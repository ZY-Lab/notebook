#Python des加密解密
###安装pydes库###
	pip install pydes
###实例化des类###
	pyDes.des(key, [mode], [IV], [pad], [padmode])
**key**：必选参数&nbsp; &nbsp;  des是对称算法，所以des的加密解密是公用一个秘钥，key为秘钥，自己设置
**model**：可选参数&nbsp; &nbsp;  加密类型，不填默认为**ECB**，建议为**CBC**，**CBC**相对于**ECB**比较安全
**IV**： 可选参数&nbsp; &nbsp;  初始值字节，**ECB**模式不需要，**BCB**模式必填，自己设置，必须8位
**pad **：可选参数&nbsp;&nbsp;  填充值，**BCB**模式和**ECB**模式都会把明文以八个分为一组进行加密，不足八个的会进行补位（一般为0或者F），**padmode**，
为**PAD_NORMAL**的时候需要填，为**PAD_PKCS5**的时候填None
**padmode**：可选参数&nbsp;&nbsp; 填充模式，分为两种模式，**PAD_NORMAL**和**PAD_PKCS5**，建议填**PAD_PKCS5**，这种模式不需要担心填充问题，加密的时候填充的部分，解密的时候他会帮你去除填充部分然后解密
###des加密###

	encrypt(data, [pad], [padmode])
**data:** 必选参数&nbsp;&nbsp; 需要加密的数据
**pad：**可选参数&nbsp;&nbsp; 同上，默认为None
**padmode：**可选参数&nbsp;&nbsp; 同上，默认为None
###des解密###

	decrypt(data, [pad], [padmode])
**data:** 必选参数&nbsp;&nbsp; 需要加密的数据
**pad：**可选参数&nbsp;&nbsp; 同上，默认为None
**padmode：**可选参数&nbsp;&nbsp; 同上，默认为None
###实例###
	import pyDes
	data = "hahaha"
	k = des("DESCRYPT", CBC, "00000000", pad=None, padmode=PAD_PKCS5)
	d = k.encrypt(data)
	print(d)
	print(k.decrypt(d))
###结果###
	b'\xdb\xd6\rb&H\x03\xdb'
	b'hahaha'
