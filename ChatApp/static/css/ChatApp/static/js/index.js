
// room-itemを選択し、roomlist変数に格納。
const roomlist = Array.from(document.querySelectorAll('.room-item'));

// HTMLの <ul id="room-list"> 中身を一旦空にする。
document.getElementById('room-list').innerHTML = '';

// チャットルームの一覧表示
for (let i = 0; i < roomlist.length; i++) {
    const eachRoom = document.createElement('li');
    eachRoom.classList.add("roomlist"); //クラス

    const roomlink = document.createElement('a');
    roomlink.href = `https://efcl.info/2022/12/15/url-cheatsheet/`; // チャットルームへのリンクを設定
    roomlink.textContent = roomlist[i].textContent;
    eachRoom.appendChild(roomlink);

    const editLink = document.createElement('a');
    editLink.href = '../templates/createroom.html'

    //今回時間が無いため、実装を断念
    // const editIcon = document.createElement('img');
    // editIcon.src = '../static/img/edit.png'; // 画像パス
    // editIcon.alt = 'ルームを編集'; // 代替テキスト
    // editIcon.width = 20; // 横サイズ（px）
    // editIcon.height = 20; // 縦サイズ（px）
    // editLink.appendChild(editIcon);
    // eachRoom.appendChild(editLink);

    // const deleteIcon = document.createElement('img');
    // deleteIcon.src = '../static/img/bin.png'; // 画像パス
    // deleteIcon.alt = 'delete'; // 代替テキスト
    // deleteIcon.width = 20; // 横サイズ（px）
    // deleteIcon.height = 20; // 縦サイズ（px']);
    // deleteIcon.addEventListener('click', function() {
    //     const confirmation = confirm (`「${roomlist[i].textContent}」を本当に削除しますか？`);
    //     if (confirmation) {
    //         eachRoom.remove();
    //         console.log(`「${roomlist[i].textContent}」は削除されました。`);
    //     }
    // });
    // eachRoom.appendChild(deleteIcon);

    document.getElementById('getChatroom').appendChild(eachRoom);
}

//掲示板の一覧表示
const bulltinboard = document.querySelectorAll('.bulltin-item');

document.getElementById('bulltinboard').innerHTML = '';
          
for (let i = 0; i < bulltinboard.length; i++) {
    const li = document.createElement('li');
    li.textContent = bulltinboard[i].textContent;
    document.getElementById('bulltinboard').appendChild(li).classList.add("bulltinboard");  
}
