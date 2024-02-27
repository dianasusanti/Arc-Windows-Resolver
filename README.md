# Arc-Windows-Resolver

Salaam everyone

(In the context of Windows Beta Release)

I tired to listen BCNY's grandious claims about their browser, Arc Browser, which they proudly dubbed as "Arc is the Chrome replacement I’ve been waiting for. (quoted from The Verge's review - which lost of context, sadly)", as even though I admit how easy and revolutionary in how it organize our browsing workflow, but it's still mediocre and sadly plegued by a crap ton of bugs which even make this holygrail unusable at all to some peoples, including ourselves.

So, as thanks to Arc Browser's community on Reddit to providing resources to locate where those problematic files which made Arc Browser unusable initially, I tried to unified the automation to at least .... make workaround to keep using Arc, while BCNY still ignorant towards these issues.

So basically, I mapped out what most frequent bugs encountered in Arc Browser which critically affected the browser usability:
- Arc Browser won't start after initial usage & closure.
- Arc Browser won't close with normal method ("X" button right-top) which prompted some users to kill it from Task Manager.

(Those issues I mentioned above mostly happened in low-end systems)

So basically this current Arc Resolver.exe covers these two issues, as I reverted the scenarious above, which is "Kills Arc first" then delete problematic folders which make Arc Browser won't start after we killing it. I make sure that this program will delete safe files that will not affected main/core experiences in using Arc.

**IMPORTANT TO NOTE:**
As this program basically written in Python, so **you're required to have Python installed on your system**. (I haven't tested it on PC which Python isn't installed, but hopefully I can, as well we will make some workaround to make it usable in that scenario)

Also worth note taking, there's major bugs which make some hearts irritated as when we close Arc with two or more windows opened and firing up Arc, it'll open with those two or more windows as previously, so I made another workaround to fix it by creating a batch file called "Multiple Windows - Arc Resolver.bat" that you can download as well from this repo.

I just really hopes for BCNY to really pay attention to these major issues as it's really affecting usability of Arc Browser for Windows. As I admit Arc is beautiful and super productive browser, also has a lot of potensials for long term. As they aimed to shoot it for general Windows users around August (Spring) 2024 and at least save Arc Browser from its potential public backlashes. You can dream big, but I begging you to see your reality and being grounded to the earth.

If there's any feedback or issue, you can contact me that you might easily find me by googling my name.

Thank you! Hope our efforts helps.

Salaam.

Diana Susanti Al Barkah & Angga Bassoni Al Barkah
