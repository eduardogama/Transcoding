import subprocess
from utils.common import update_dir_version


def create_elastic_transcoder_hls_job(pipeline_id, input_file,
                                      outputs, output_file_prefix,
                                      playlists):
    """Create an Elastic Transcoder HSL job

    :param pipeline_id: string; ID of an existing Elastic Transcoder pipeline
    :param input_file: string; Name of existing object in pipeline's S3 input
    :param outputs: list of dictionaries; Parameters defining each output file
    # :param output_file_prefix: string; Prefix for each output file name
    :param playlists: list of dictionaries; Parameters defining each playlist
    :return Dictionary containing information about the job
            If job could not be created, returns None
    """
    pass


def main():

    transcoder_params = {
        'output_path': '/home/eduardo/GitHub/dev/Transcoder/vod/',
        'input_path': '/home/eduardo/Videos/',
        'movie': 'bbb_sunflower',
        'filename': 'bbb_sunflower_1080p_60fps_normal.mp4',
    }

    print('Running Trancoder ...')

    update_dir_version(transcoder_params)

    download_path = transcoder_params['input_path'] + transcoder_params['filename']
    filename = transcoder_params['output_path'] + transcoder_params['movie'] + '/' + transcoder_params['movie']

    # call FFmpeg directly
    cmd = f'ffmpeg -i {download_path} -codec: copy -start_number 0 \
        -hls_time 10 -hls_list_size 0 -f hls {filename}.m3u8'

    process = subprocess.run(cmd, shell=True, capture_output=True)
    if process.returncode == 0:
        print("Transcoding Video Successed !")


if __name__ == '__main__':
    main()
