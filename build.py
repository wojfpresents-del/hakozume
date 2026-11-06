# ゲーム本体(hakozume.html：アーティファクト用の断片)から、GitHub Pages用の完全なindex.htmlを作る
import sys,re
src=open(sys.argv[1],encoding='utf8').read()
src=src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
i=src.index('</style>')+len('</style>')
head,body=src[:i],src[i:]
out=('<!doctype html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n'
 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
 '<meta name="robots" content="noindex, nofollow">\n'
 '<meta name="theme-color" content="#ffeccc">\n<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Ctext y=%22.9em%22 font-size=%2290%22%3E%F0%9F%93%A6%3C/text%3E%3C/svg%3E">\n<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-title" content="ハコヅメ">\n<meta property="og:title" content="ハコヅメ">\n<meta property="og:description" content="中の見えない入れ物に順番に物を詰める、溢れさせたら負けのパーティーゲーム。スマホでオンライン4人対戦も">\n<meta property="og:type" content="website">\n'
 '<meta name="description" content="中の見えない入れ物に順番に物を詰めていく、溢れさせたら負けのパーティーゲーム">\n'
 +head+'\n</head>\n<body>\n'+body.strip()+'\n</body>\n</html>\n')
open('index.html','w',encoding='utf8').write(out)
