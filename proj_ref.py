shared_folder = {
    'aloeber': '/content/drive/MyDrive/207-Project'    
    , 'aminaalavi': '/content/drive/MyDrive/207-Project'
    , 'hamsini.sankaran': '/content/drive/MyDrive/UCB-MIDS/SEM-2/MACHINE-LEARNING-207/207-Project'
    , 'rachelgao': '/content/drive/MyDrive/207/207-Project'
}

files = {
    'taxonomy':             'BirdCLEF/eBird_Taxonomy_v2021.csv'
    , 'orig_metadata':      'BirdCLEF/train_metadata.csv'
    , 'sample_metadata':    'data/sample_metadata.csv'
    , 'species_metadata':   'data/species_metadata.csv'
    , 'train_metadata':     'data/train_metadata.csv'
    , 'test_metadata':      'data/test_metadata.csv'
}

dirs = {
    'orig_audio': {
        'path':       'BirdCLEF/train_audio'
        , 'file_ext': '.ogg'
    }
    
    , 'train_audio': {
        'path':       'data/train/audio_files'
        , 'file_ext': '.ogg'
    }
    
    , 'test_audio': {
        'path':       'data/test/audio_files'
        , 'file_ext': '.ogg'
    }
    
    , 'train_npy_full': {
        'path':       'data/train/librosa_loaded'
        , 'file_ext': '.npy'
    }
    
    , 'test_npy_full': {
        'path':       'data/test/librosa_loaded'
        , 'file_ext': '.npy'
    }
    
    , 'train_npy_loud5s': {
        'path':       'data/train/librosa_loaded_loudest_5sec'
        , 'file_ext': '.npy'
    }
    
    , 'test_npy_loud5s': {
        'path':       'data/test/librosa_loaded_loudest_5sec'
        , 'file_ext': '.npy'
    }
}
