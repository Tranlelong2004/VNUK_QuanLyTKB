# VNUK_QuanLyTKB
git branch develop: tạo nhánh develop
git checkout develop: qua nhánh develop
git branch: xem đang ở nhánh nào

git push -u origin develop: tạo copy giống main để code tiếp

git checkout -b feature/1-add-cart develop:
-b: tạo nhánh mới và check out qua nhánh lun
- develop: là tạo nhánh feature trong nhánh develop

git status: xem trạng thái của file

git commit -m "#1 - Long add cart": 
commit với nội dung là #1 - Long add cart
--> git push


git pull : kéo về nhánh develop# VNUK_QuanLyTKB



git tag 'v1.0.0': tạo tag v1.0.0
git push --tags: tao tag lên remote len 

git merge develop: gộp nhánh develop vào nhánh hiện tại
git branch -d   feature/1-add-cart-model: xoá nhánh feature/1-add-cart-model

git fetch origin
