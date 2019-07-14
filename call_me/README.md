# Call Me
File: [call_me](call_me)

Run the file:
```
# ./call_me

There is nothing...
Bye!
```
Running `strings`:
```
# strings call_me | grep Inno
/home/master/Documents/Projects/InnoCTF2019/Ural2018/Call me by my name
```
Running `readelf -s call_me` saw a function called `flag`:
```
# readelf -s call_me 
66: 00000000000014f3    39 FUNC    GLOBAL DEFAULT   13 main
67: 0000000000004040     0 OBJECT  GLOBAL HIDDEN    23 __TMC_END__
68: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
69: 0000000000001159   922 FUNC    GLOBAL DEFAULT   13 flag
70: 0000000000000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@@GLIBC_2.2
71: 0000000000001000     0 FUNC    GLOBAL HIDDEN    11 _init
```
The challenge named `Call me` I guess we can call the function 

After a quick google search, we found gdb can done [this](https://stackoverflow.com/questions/1354731/how-to-evaluate-functions-in-gdb)

```
# gdb call_me
...
...
pwndbg> break main
Breakpoint 1 at 0x1502: file var 2.c, line 20.
pwndbg> run
Starting program: /root/Downloads/InnoCTF2019/call_me/call_me 

Breakpoint 1, main (argc=1, argv=0x7fffffffe188) at var 2.c:20
...
...
...
 ► f 0     555555555502 main+15
   f 1     7ffff7e0809b __libc_start_main+235
Breakpoint main
pwndbg> call flag()

Your flag:
InnoCTF{How_d1d_y0u_f1nd_m3_7f1bc88}�
$1 = 39
```

# Flag
> InnoCTF{How_d1d_y0u_f1nd_m3_7f1bc88}