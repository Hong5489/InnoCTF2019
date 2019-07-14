# One Hundred Times RSA
```
Message = 540044793906259530810264019597753740811399829200787379697611542563373670397414734352341760520668884
Modulus = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
```
Modulus means `n` in RSA

Looks like `n` is small, lets try to factorize it!

I used FactorDB to help me:
```
http://factordb.com/index.php?query=1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
```
Result: 37975227936943673922808872755445627854565536638199 * 40094690950920881030683735292761468389214899724061

Means `p` and `q` was found! (Because `n = p*q`)

Lets calculate `d` and decrypt it using Python!
```python
from Crypto.Util.number import inverse
n = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
p = 37975227936943673922808872755445627854565536638199
q = 40094690950920881030683735292761468389214899724061
c = 540044793906259530810264019597753740811399829200787379697611542563373670397414734352341760520668884
e = 65537
phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(c,d,n)
print hex(m)
```
Result:
```
0xb586ba73873a722e00f91bfd6de2767b17c434dcb1e1e2428fb67f2a0a0276792c34517e3afb8e2e97L
```
You can see the hex value is not in ASCII range

I must be doing something wrong,

At first, I taught I need to decrypt 100 times because the challenge title say so

But I realized `e` is not given, maybe we need to guess the `e` value (public key)

Wrote a [python script](solve.py) to brute force the `e`:
```python
for e in range(65537):
	d = inverse(e,phi)
	m = pow(c,d,n)
	text = hex(m)[2:].replace('L','')			# remove the 'L' in last character
	if len(text) % 2 != 0:						
		text = '0'+text						# If length not even add a '0' infront
	if text.decode('hex').startswith("InnoCTF"):
		print "e = " + str(e)
		print text.decode('hex')
```
After couple seconds, found **e = 47131** and decrypted the flag!

# Flag
> InnoCTF{cr4ck_rs4_4g41n_08a5}