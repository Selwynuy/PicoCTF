# morse-code
## Description
Morse code is well known. Can you decrypt this?
Download the file here.
Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.
## Hint
Audacity is a really good program to analyze morse code audio.
## Solution

The challenge gives out a morse code and upon checking with audacity I got this morse code

![image](https://github.com/Selwynuy/PicoCTF/assets/107299589/b5b0c289-82ef-4b48-bcfe-a5f14d1ba68a)

Then wrote it down

```
.-- .... ....- --...  .... ....- --... ....  ----. ----- -..  .-- ..--- ----- ..- ----. .... --...
```
I used this site to decode the message: http://www.unit-conversion.info/texttools/morse-code/

Result:
```
wh47?h47h?90d?w20u9h7
```

Flag: PicoCTF{wh47_h47h_90d_w20u9h7}
