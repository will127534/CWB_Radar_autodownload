from tqdm import tqdm
import requests
import time
import os 
BaseUrl_1 = "http://61.56.11.42/nidsB/images/QPESUMSgoogle/cref2d_rad/COMPREF."
"yyyymmdd.hhmm"
BaseUrl_2 = ".LST.png"

archfiles = os.listdir(".")


timestart = time.time()-86400*7
time_st = time.struct_time(time.localtime(timestart))
timestart = timestart - ((time_st[4]%10)*60 + time_st[5])
while timestart<time.time()-600:
    
    timestring = time.strftime("%Y%m%d.%H%M",time.localtime(timestart))
    url = BaseUrl_1+ timestring + BaseUrl_2
    filename = time.strftime("%Y%m%d_%H%M",time.localtime(timestart))+ ".png"
    print "Finding " + filename
    if (filename not in archfiles):
        print("Downloading %s as %s \r\n" % (url,filename))
        response = requests.get(url, stream=True)
        with open(filename , "wb") as handle:
            for data in tqdm(response.iter_content(1024*100)):
                handle.write(data)
        pass
    timestart = timestart +600
    pass

print "finish downloading last 7 days data"
t = time.time()
time_st = time.struct_time(time.localtime(t))
t = t - ((time_st[4]%10)*60 + time_st[5])
t = t + 540
print "Sleep until" +  time.strftime(" %Y%m%d %H:%M:%S", time.localtime(t))
print "Sleep" + str(t -time.time())
time.sleep(t -time.time())

while 1:
    t = time.time()
    time_st = time.struct_time(time.localtime(t))
    t = t - ((time_st[4]%10)*60 + time_st[5])
    timestring = time.strftime("%Y%m%d.%H%M", time.localtime(t))
    url = BaseUrl_1+ timestring + BaseUrl_2
    filename = time.strftime("%Y%m%d_%H%M", time.localtime(t))
    print("Downloading %s as %s \r\n" % (url,filename))
    response = requests.get(url, stream=True)
    with open(filename+ ".png" , "wb") as handle:
        for data in tqdm(response.iter_content(1024*100)):
            handle.write(data)

    t = t + 540 +600
    print "Sleep until" +  time.strftime(" %Y%m%d %H:%M:%S", time.localtime(t))
    print "Sleep" + str(t -time.time())
    time.sleep(t -time.time())

