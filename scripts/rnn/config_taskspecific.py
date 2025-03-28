from dataclasses import dataclass
from config import Basic_Config

@dataclass
class debug_Config(Basic_Config):
    vocab = ['<pad>', 'a', 'b', '1', '2', '3']
    
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