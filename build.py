# ゲーム本体(hakozume.html：アーティファクト用の断片)から、GitHub Pages用の完全なindex.htmlを作る
import sys,re
src=open(sys.argv[1],encoding='utf8').read()
src=src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
i=src.index('</style>')+len('</style>')
head,body=src[:i],src[i:]
out=('<!doctype html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n'
 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
 '<meta name="theme-color" content="#ffeccc">\n<meta name="description" content="中の見えない入れ物に順番に物を詰めていく、溢れさせたら負けのパーティーゲーム">\n'
 +head+'\n</head>\n<body>\n'+body.strip()+'\n</body>\n</html>\n')
open('index.html','w',encoding='utf8').write(out)
