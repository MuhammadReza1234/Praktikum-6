p=print
p('pertemuan 10')
p('nama\t: rini ariza\nkelas\t: TI.22.A3\nNIM\t: 312110337\n')

b={'ari':'085267888','dina':'087677776'}
p('Kontak awal')
p('==============================')
p('#    nama    |   nomor telepon')
p('==============================')
p('#    ari     |   085267888','\n#    dina    |   087677776')

# tampilkan kontak ari
p('\nTampilkan Kontak Ari')
p('#    ari     |   ',b['ari'])

p('\nMenambah Kontak Riko')
b['riko']='087654544'
p('#    ari      |   ',b['ari'])
p('#    dina     |   ',b['dina'])
p('#    riko     |   ',b['riko'])

p('\nMengubah nomor Dina ke')
b['dina']='088999776'
p('#    ari      |   ',b['ari'])
p('#    dina     |   ',b['dina'])
p('#    riko     |   ',b['riko'])

p('\nMenampilkan semua nama')
p(b.keys())

p('\nMenampilkan semua nomor')
p(b.values())

p('\nMenampilkan semua nama dan nomor')
p(b)

p('\nMenghapus kontak dina')
del b['dina']
p(b)