# Self-Yuie

## Setup 

### - Download files : https://github.com/antjules27/Self-yuie/archive/refs/heads/main.zip
  * Extract files in a folder

### - get your account token
  * Go on Web Discord on desktop https://discord.com/login
  * do Ctrl + Shift + i to open web Dev tool 
    ![image](https://user-images.githubusercontent.com/45826872/203141081-93249531-bad4-40b5-9968-84884c05dffe.png)
  * go on the top right corner and click on app (ou appli depends on your language) section(and enable phone screen mode with the phone and tablet icon)
   > if you don't see it, try to click on the ">>" arrows.

 ![image](https://user-images.githubusercontent.com/45826872/203142257-2d9fbd50-f51c-4750-b403-1463be402a7c.png)

  * You should see something called "local storage", expand it and you get https://discord.com.
  
 ![image](https://user-images.githubusercontent.com/45826872/203142797-578ad57b-726d-4649-a821-3df42fec692c.png)

  * then you get your token, searc and just click and copy it.
  ![image](https://user-images.githubusercontent.com/45826872/203143127-ce7283e3-9610-4ffe-9571-3356645822a5.png)
  > if you don't see it use filters and type "token"
  
  
  
 ## Configuration 

  * you juste have to put your token into the **token.id** file in /config/ folder. 
  * if you use an another account as a Selfbot, i recommend you to put also in the id.id file your personal discord id and disable "selfing" option in **share.conf**.
  > to get it in discord desktop/web just right click on your profile in your dms or in a group and click copy id. 
  
  * you can choose to configure **share.conf** wich is use to tell the bot to who he can answer commands. 
  * You can choose to configure **prefixes.conf**, theses are the prefixes you will use in order to do any commands. 
   > by default it's "." and ">"
   
  ## Usage 
  
  - ping command
  ```py 
     .ping
  ```
  > get bot pong in ms
 
 - embed command
  ```py 
     .embed {title = your title ; description=your description ; author=your author text ; color=255,255,255; image=https://test.com/yourimage.jpg; url=https://google.fr }
  ```
  > to make really cool embed ! 
 
  
  
  
