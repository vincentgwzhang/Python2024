import time

print(time.time())

t = time.localtime()
print(f'Now is {t.tm_year}-{t.tm_mon}-{t.tm_mday} {t.tm_hour}:{t.tm_min}:{t.tm_sec}')
print(time.strftime('Now is %Y-%m-%d %H:%M:%S', t))