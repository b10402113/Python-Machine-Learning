## 首次操作git - 創建repo （首次要這樣做）

1. 先創立資料夾，在終端機打上

```git init
git init
```

2. 新增檔案與提交

```
git add . // 新增全部有更改的檔案
git commit -m "訊息" // 提交你的檔案到本地端
```

3. 設定與git連接的GitHub repo 

```
git remote add origin https//....git 
```

4. 將資料push上github 

```git
git push -u origin master
```

## 第二次跟之後要上傳資料-三部曲

1. git add [資料名稱]

```
git add . // 新增全部修改的資料
git add [名稱] // 新增部分修改的資料
```

2. git commit -m "說明"

```
git commit -m "說明"
```

3. 將資料放到雲端

```
git push
```

## 下載別人的git Repo

（第一種）clone

1. clone一個git repo

```
git clone https://.. 我就愛改名 
```

2. 更新別人的repo

```
git pull
```

（第二種）fork

1. fork別人的repo會到自己的github也看到那個repo
2. 自己的repo可以自己爽爽修改
3. 更新別人的repo

```
remote add upstream https: //別人的repo
git pull upstream 
```

