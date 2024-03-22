# Penguin Brawl
Open source Python 3.8 Brawl Stars Server for version 12!
![ScreenShot](https://cdn.discordapp.com/attachments/1216025567808454717/1220719918568312873/Imagem_do_WhatsApp_de_2024-03-22_as_09.52.19_cf501cb1.jpg?ex=660ff704&is=65fd8204&hm=f33cab8e7fedc93ad8b212c22c2197b0b53c43c8cc6e6f9f7933850d07a61e8c&) 

## Setup
First you must install TweetNaCl. To do it use this command: ```python setup.py install --user```.
Now you can run server. If your OS is Windows just run main.py. If Linux type ```python3 main.py``` to terminal.

## Client
To connect to your server, you need a custom client. Here the only solution is to use a [pre-made client](https://drive.google.com/file/d/1-K95h2eWZRK6RtfR2cnxTrKCU9S8kiVC/view).
Just edit the IP in the frida-gadget config (```/lib/armeabi-v7a/liblover.config.so```)
```{
   "interaction": {
      "type": "script",
      "path": "liblover.script.so",
      "on_change": "reload",
      "parameters": {
         "redirectHost": "127.0.0.1",
         "redirectPort": 9339,
         "toast": "Server By LibraryLover",

         "credit": "t.me/haccythalesco or thalesco.haccer"
      }
   }
}```

## Authors

👤 **Mr Vitalik** (main developer)

* Github: [@VitalikObject](https://github.com/VitalikObject)

👤 **xeonnnnn** (main developer)

* Github: [@xeonnnnn](https://github.com/xeonnnnn)

👤 **PhoenixFire** (passive)

* Github: [@PhoenixFire6934](https://github.com/PhoenixFire6934)

👤 **Icaro**

* Github: link deprecated

👤 **ThalesGithubUser**
 Me For Patching The Client
### Friendly reminder
The server is in a very early state. Right now, it is NOT recommended to run this on a production environment. Please not open issues about missing features, i'm well aware of this. 

#### Need help? Join [My Discord server](https://discord.gg/4FZrUFK4C6)
If You Want
