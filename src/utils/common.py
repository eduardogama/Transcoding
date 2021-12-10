import os


def update_dir_version(transcoder_params):
    path = transcoder_params['output_path']
    movie = transcoder_params['movie']

    if not os.path.exists(path + movie):
        print('Directory doesnt exist... Creating Directory.')
        os.mkdir(path + movie)
