import torch, json
import numpy as np

def sequences_collator(texts, w2i, max_seq_len):
    input_ids = []
    labels = []
    for t in texts:
        i, l = json.loads(t['text'])
        
        input_id = [w2i[w] for w in i]
        input_id += [w2i['<pad>']] * (max_seq_len - len(input_id))

        label = [w2i[w] if not w == '-1' else -1 for w in l]
        label += [-1] * (max_seq_len - len(label))

        input_ids.append(input_id)
        labels.append(label)
        
    return {
        'input_id': torch.LongTensor(input_ids),
        'label': torch.LongTensor(labels),
        'position_id': torch.LongTensor([[]]),
        'attention_mask': torch.tensor([[]]),
    }

def get_acc(logits, labels, ignore_index):
    pred = logits.argmax(dim=-1)

    correct, demo = 0, 0

    for _pred, _labels in zip(pred, labels):
        pred = _pred[_labels != ignore_index] #[-1].squeeze()
        label = _labels[_labels != ignore_index] #[-1].squeeze()

        correct += (pred == label).float().sum().item()
        demo += label.numel()

    return correct, demo 


def inference(model_to_eval, dataloader, criterion, device, vocab):
    
    correct, demo = 0, 0
    losses = []
    testing_output = {}
    k = 0
    for i, batch in enumerate(dataloader):
        position_ids = None
        if batch['position_id'] is not None: position_ids = batch['position_id'].to(device)
        logits = model_to_eval(
            batch['input_id'].to(device),
            position_ids = position_ids,
            attention_mask = batch['attention_mask'].to(device),
        )
        
        batch['label'] = batch['label'].to(device)
        loss = criterion(
            logits.view(-1, logits.size(-1)), # bs*seq_len, vocab_size
            batch['label'].view(-1), # 1, bs*seq_len
        )
        losses.append(loss.detach().item())
        _correct, _demo = get_acc(
            logits.detach().cpu(), 
            batch['label'].detach().cpu(), 
            ignore_index=-1,
        )
        correct += _correct
        demo += _demo

        for input_id, gth_id, pred_id in zip(batch['input_id'], batch['label'], logits.argmax(dim=-1)):
            input_seq = [vocab[i] for i in input_id if vocab[i]!='<pad>']
            gth_seq = [vocab[gth_id[i]] for i in range(len(gth_id)) if gth_id[i]!=-1]
            pred_seq = [vocab[pred_id[i]] for i in range(len(gth_id)) if gth_id[i]!=-1][:len(gth_seq)]
            testing_output[k] = {
                "input": " ".join(input_seq),
                "gth": " ".join(gth_seq),
                "pred": " ".join(pred_seq),
            }
            k+=1

    avg_loss = round(np.mean(losses), 4)
    avg_acc = round(correct/demo, 4)
    print(f"num_test = {k}")

    return avg_loss, avg_acc
    