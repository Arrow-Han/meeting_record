import ffmpy

source_file = r"../../docu/test_video.MOV"
sink_file = r"../../final/document/mp4_output_test-video.mp4"

ff = ffmpy.FFmpeg(
    inputs={source_file: None},
    outputs={sink_file: None}

)
ff.run()