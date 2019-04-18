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

##git情境劇

如何將檔案從 Stage 中移除(取消add)

`git reset HEAD 檔案名稱`



`git reset HEAD^ --soft` 取消剛剛的 commit，但保留修改過的檔案。

`git reset HEAD^ --hard` 取消剛剛的 commit，回到再上一次 commit的 乾淨狀態。



- `git branch` 列出所有本地端的 branch。
- `git branch -r` 列出所有遠端的 branch。
- `git branch -a` 列出所有本地及遠端的 branch。
- `git branch "branch名稱"` 建立一個新的 branch。
- `git checkout -b "branch名稱"` 建立一個新的 branch 並切換到該 branch。
- `git branch branch名稱 起始點` 以起始點作為基準建立一個新的 branch，起始點可以是一個 tag，branch 或是 commit。
- `git branch --track branch名稱 遠端branch` 建立一個 tracking 遠端 branch 的 branch，這樣以後 push/pull都會直接對應到該遠端的branch。
- `git branch --set-upstream branch 遠端branch` 將一個已存在的 branch 設定成 tracking 遠端的branch。
- `git branch -d "branch 名稱"` 刪除 branch。
- `git -r -d 遠端branch` 刪除一個 tracking 的遠端 branch，例如`git branch -r -d wycats/master`
- `git push repository名稱 :遠端branch` 刪除一個 repository 的 branch，通常用在刪除遠端的 branch，例如`git push origin :old_branch_to_be_deleted`。
- `git checkout branch名稱` 切換到另一個 branch(所有修改過程會被保留)。

1. 遠端操作(remote)
   - `git remote add remote名稱 remote網址` 加入一個 remote repository，例如 `git remote add github git://github.com/gogojimmy/test.git`
   - `git push remote名稱 :branch名稱` 刪除遠端 branch，例如 `git push origin :somebranch`。
   - `git pull remote名稱 branch名稱` 下載一個遠端的 branch 並合併(注意是下載遠端的 branch 合併到目前本地端所在的 branch)。
   - `git push` 類似於 pull 操作，將本地端的 branch 上傳到遠端。
2. 合併操作(merge)
   - `git merge branch名稱` 合併指定的 branch 到目前的 branch。
   - `git merge branch名稱 --no-commit` 合併指定的 branch 到目前的 branch 但是不會產生合併的 commit。
   - `git cherry-pick SHA` 將某一個 commit 的內容合併到目前 branch，指定 commit 是使用該 commit 的 SHA 值，例如 `git cherry-pick 7300a6130d9447e18a931e898b64eefedea19544`。
3. 暫存操作(stash)
   - `git stash` 將目前所做的修改都暫存起來。
   - `git stash apply` 取出最新一次的暫存。
   - `git stash pop` 取出最新一次的暫存並將他從暫存清單中移除。
   - `git stash list` 顯示出所有的暫存清單。
   - `git stash clear` 清除所有暫存。
4. 常見問題：
   - 我的 code 改爛了我想全部重來，我要如何快速回到乾淨的目錄?
     - `git reset --hard` 這指令會清除所有與最近一次 commit 不同的修改。
   - merge 過程中發生 confict 我想放棄 merge，要如何取消 merge？
     - 一樣使用 `git reset --hard` 可以取消這次的 merge。
   - 如何取消這次的 merge 回到 merge 前的狀態?
     - `git reset --hard ORIG_HEAD` 這指令會取消最近一次成功的 merge 以及所有你在這次 merge 後所做的修改。
   - 如何回復單獨檔案到原本 commit 的狀態?
     - `git checkout 檔案名稱` 這指令會將已經被修改過的檔案回復到最近一次 commit 的樣子。
5. 其他連結：
6. [Git 教學(1)：Git的基本使用](http://blog.gogojimmy.net/2012/01/17/how-to-use-git-1-git-basic/)
7. [Git 教學(2)：Git Branch 的操作與基本工作流程](http://blog.gogojimmy.net/2012/01/21/how-to-use-git-2-basic-usage-and-worflow/)
8. [Git 情境劇：告訴你使用 Git 時什麼情況該下什麼指令](http://blog.gogojimmy.net/2012/02/29/git-scenario/)

Posted by Jimmy Kuo Feb 29th, 2012  [git](https://blog.gogojimmy.net/blog/categories/git/)