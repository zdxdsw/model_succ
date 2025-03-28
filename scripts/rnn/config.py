from dataclasses import dataclass

@dataclass
class Basic_Config:
    seed = 929
    model = "RNN"
    date = "debug"
    hf_cache_dir = '/data/yingshac/hf_cache'
    num_hidden_layers = 1
    vocab = []
    task = ""
    gendate = ""
    aux_tasks = []
    hidden_size = 16
    max_seq_len = 60
    freeze_null_emb = False
    dropout = 0.1
    tie_word_embeddings = False
    initializer_range = 0.02
    output_dir = "output"
    ckpt_dir = "/data/yingshac/model_succ/scripts/rnn/output"
    train_data_path = "/data/yingshac/model_succ/data/"
    eval_data_path = "../../data/"
    test_files = [""]
    per_device_train_batch_size = 32
    gradient_accumulation_steps = 1
    per_device_eval_batch_size = 64
    eval_accumulation_steps = 1
    logging_steps = 200
    #warmup_steps = 0 #3000
    learning_rate = 0.01
    weight_decay = 0.01
    num_epochs = 5
    eval_every_steps = 100000 # useless for now
    load_from_dir = None #"0427_131257" # 
    init_from_ckpt = None


@dataclass
class Default_Config:
    seed = 1234
    tie_word_embeddings = False
    initializer_range = 0.02
    model = "RNN"
    freeze_null_emb = False
    hf_cache_dir = None