import h5py
f_overhang = h5py.File("./data/overhang/bae8f52c-407e-5f89-a8e3-61fcca51ee0a_raw.h5", "r" )
print (list(f_overhang.keys()))

acc_LH_Jona = f_overhang["acc_LH"]

print(acc_LH_Jona.shape)
#print (list(acc_LH_Jona))

print ("done")