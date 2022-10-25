import vapoursynth as vs
core = vs.core

core.num_threads = 16
core.max_cache_size = 2000

vfile = r'XXX.mp4'
src = core.lsmas.LWLibavSource(vfile)
#VFRtoCFR must in English path
tcfile = r'timecode.txt'#指定timecode文件位置
src = core.vfrtocfr.VFRToCFR(src, timecodes=tcfile, fpsnum=24000, fpsden=1001)#将视频转换为指定固定帧率

src.set_output() 