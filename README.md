# liammulh.net

On Ubuntu using Node 18, it seems we have to create a symlink to the
`eleventy.js` script:

```
ln -s ./node_modules/eleventy/eleventy.js ./node_modules/.bin/eleventy
```
