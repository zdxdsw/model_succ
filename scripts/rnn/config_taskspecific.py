from dataclasses import dataclass
from config import Basic_Config

@dataclass
class debug_Config(Basic_Config):
    vocab = ['<pad>', 'a', 'b', '1', '2', '3']

@dataclass
class model_succ1_10_20_Config(Basic_Config):
    vocab = [str(i) for i in range(22)] + ['+', '-', '#', '<sep>', '<eos>', '<pad>']
    test_files = ["test"]

@dataclass
class model_succ2_3_20_Config(Basic_Config):
    vocab = list(map(chr, range(97, 123))) + ['+', '-', '#', '<ns>', '<sep>', '<eos>', '<pad>']
    test_files = ["test"]

@dataclass
class model_succ2_3_50_Config(Basic_Config):
    vocab = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91))) + ['+', '-', '#', '<ns>', '<sep>', '<eos>', '<pad>']
    test_files = ["test"]

@dataclass
class model_succ2_10_20_Config(Basic_Config):
    vocab = list(map(chr, range(97, 123))) + ['+', '-', '#', '<ns>', '<sep>', '<eos>', '<pad>']
    test_files = ["test"]

@dataclass
class model_succ3_2_50_Config(Basic_Config):
    vocab = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91))) + ['+', '-', '#', '<ns>', '<sep>', '<eos>', '<pad>']
    test_files = ["test"]

@dataclass
class model_succ3_3_50_Config(Basic_Config):
    vocab = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91))) + ['+', '-', '#', '<ns>', '<sep>', '<eos>', '<pad>']
    test_files = ["test"]

@dataclass
class dyck1_1_Config(Basic_Config):
    vocab = ['(', ')', '1', '0','<pad>']
    test_files = ["val_20_40", "val_40_60"]

@dataclass
class dyck1_2_Config(Basic_Config):
    vocab = ['(', ')', '1', '0','<pad>']
    test_files = ["val_20_40", "val_40_60"]

@dataclass
class dyck1_3_Config(Basic_Config):
    vocab = ['(', ')', '1', '0','<pad>']
    test_files = ["val_20_40", "val_40_60"]

@dataclass
class dyck1_4_Config(Basic_Config):
    vocab = ['(', ')', '1', '0','<pad>']
    test_files = ["val_20_40", "val_40_60"]

@dataclass
class dyck1_12_Config(Basic_Config):
    vocab = ['(', ')', '1', '0','<pad>']
    test_files = ["val", "val_dyck1_2", "val_dyck1_3", "val_dyck1_4", "val_dyck1_5"]

@dataclass
class dyck1_123_Config(Basic_Config):
    vocab = ['(', ')', '1', '0','<pad>']
    test_files = ["val", "val_dyck1_2", "val_dyck1_3", "val_dyck1_4", "val_dyck1_5"]

@dataclass
class dyck1_1234_Config(Basic_Config):
    vocab = ['(', ')', '1', '0','<pad>']
    test_files = ["val", "val_dyck1_2", "val_dyck1_3", "val_dyck1_4", "val_dyck1_5"]