# Goat-Rulings

This site is meant to streamline the process of looking up a ruling for Yu-Gi-Oh!'s Goat and Edison formats. Find the rulings for "Thousand-Eyes Restrict" here: https://www.goatformat.com/indivrulings.html.  
Come back and try the same thing: https://joshuabones.github.io/Goat-Rulings/

## Planned features

Better formatting for desktop  
Clean up code, move to more components

## How it was made

Vue.js + Vite 
https://vitejs.dev/guide/

Deployed on github pages 
https://www.youtube.com/watch?v=yo2bMGnIKE8

Data was ripped from these two links with python: https://www.goatformat.com/indivrulings.html 
https://www.edisonformat.com/rulings

From a YouTube comment:
```
To recommit new changes and push up to the remote repository:

1. On remote repository delete the "gh-pages" branch. 

2. In you local repository run this command: npm run build (1:56)

3. git add dist -f (2:05)

4. git commit -m [your commit message here] (2:17)

5. git subtree push --prefix dist origin gh-pages (2:20)
```
