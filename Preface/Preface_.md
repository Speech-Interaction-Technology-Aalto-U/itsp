# Preface

This is a collection of pedagogical material within the topic of speech
and language technology. The idea is to provide

-   teachers material for their courses, where they can pick and choose
    material which is appropriate for their own courses.
-   self-study material on-line for anyone interested.

By licensing the material under creative commons (share alike), we want
to encourage people to contribute improvements and additions to the
content.


## Design philosophy of this document

-   Target audience
    -   Primary target:
        -   Master's level students with some background in digital
            signal processing (=signals and systems), machine learning,
            linear algebra and stochastic processes
    -   Secondary targets:
        -   Researchers in related areas who want to expand their
            expertise, for example, researchers in machine learning,
            signal processing, audio processing, linguistics,
            human-computer interfaces etc
-   Keep a pedagogical approach
    -   Explain why this tool is needed and how it solves a problem.
    -   Give an example of how it is used in practice, including
        demonstrations and pictures.
    -   Favour tools which everyone are using, rather than inventions of
        your own team
-   Small steps
    -   Better to have something than nothing. Though it is a good
        direction, reaching perfection is not a requirement.
    -   Fix errors immediately when you find one.



## Foreword to the First Edition

Foreword by Tom Bäckström

As I was teaching the course "Speech processing" at Aalto University, I
was always looking for good teaching material. I was not really content
with what I found. Some good books were available but they were
expensive. I was not comfortable with demanding the students to pay
hundreds of Euros for a book they'd use once. I was also not comfortable
in illegally copying content. The alternatives were then to accept
lower-quality material or write my own.

Part of the issue I have with expensive books is that the money does not
go to the authors themselves, but to middle-men. Moreover, in the
Internet-era, paper books seem so last-century. Why print a book on
paper when we can make it a web document? Why put it behind a pay-wall?
I mean, I really would not receive any significant part of my income
from such a book. Putting it on the web then seems like the only sane
solution.

Besides, once you're free from the constraints of a conventional book,
you can do all kinds of fun stuff. Like why would I limit access to
modifying content and why not something more wikipedia-like? I'm paid by
the government, so it seems also obvious that I should put my work out
in the public domain. No, more accurately, I'm putting this out with a
Creative Commons licence (attribution & share-alike). Perhaps it's
vanity, but I would like to receive credit for this work, if there is
any credit due.

The desired consequence of Creative commons licensing is that the
material would find multiple contributors, to improve the content. To
follow the old, worn but accurate adage; to stand on the shoulders of
giants, and so forth. By collaboration we can do better.


The way I intend to use this in my own teaching is that the on-line
version of the document follows its own natural grouping of topics.
Start with basics and progress to more complex topics and applications.
For my own, course, however, I want to have exercises in parallel with
the course. The problem is then that the most basic chapters do not lend
themselves to exercises which are useful for my teaching goals. So I
design exercises to match my teaching goals and organize lecture
material to give sufficient background to the exercises. In this
web-based document this is no problem. I'll just create a new table of
contents, where the ordering of chapters and sections is reorganized.


    
## Foreword to the 2nd Edition

Foreword by Tom Bäckström

I have been positively encouraged and surprised by the feedback I have received for the first edition. So many people have spontaneously given feedback. I find it safe to assume that many more have used this material than those who have contacted me. I therefore conclude that the impact of this material has been much larger than I anticipated. Great! This encourages me to continue putting effort into the document, to make it better and expand it.

For the second edition, I wanted to address the following issues:

- Platform:

    - Integration with [JupyterLab](https://jupyter.org/) and other similar platforms for interactive coding examples and visualizations are not easily possible on the original platform. Still, in my own teaching I have found such tools mmensly effective and popular among the students.
    - Though the material was published as Open access with a Creative Commons license, the original platform did not allow for easy porting to other formats. Especially mathematical notation and equations required extra effort when porting. This is a clear contradiction to our open access intentions and desires. 

   Clearly both arguments lead to the conclusion that we have to switch platforms. Delaying the switch further will make it only harder. Currently the dominant way of sharing evovling community projects is [git](https://en.wikipedia.org/wiki/Git) and consequently, that is the obvious choice. Additional benefits from git-based platforms is that they have many practical tools integrated, like merge-requests, discussion boards etc.

- Content:

    - Machine learning in speech processing was not well-enough represented. Have to add and improve the content in that area. 
    - I am developing and have recently particpated in generation of additional content both for a Bachelor-level introductory course as well as a course about design of speech interaction technology. Those should be added here.
    - There are also many other areas which would benefit from additions, like speech recognition and NLP. I hope we find someone to contribute material also there.
