
//ユーザーネームの取得と表示
let username = "testuser"; //定義されていないと実行されない
    document.getElementById('loginMessage').textContent = `${username}さん、お仕事お疲れ様です。`;


//チャットルームの一覧表示
const roomlist = ['チームチャットルーム', '経理財務連携チャットルーム', 'かずきさん', '同期チャットルーム', 'レクリエーション', 'チームチャットルーム', '経理財務連携チャットルーム', 'かずきさん', '同期チャットルーム', 'レクリエーション', 'チームチャットルーム', '経理財務連携チャットルーム', 'かずきさん', '同期チャットルーム', 'レクリエーション']
              
    for (let i = 0; i < roomlist.length; i++) {
    const eachRoom = document.createElement('li');
    eachRoom.classList.add("roomlist"); //CSSクラス

    const roomlink = document.createElement('a');
    roomlink.href = `https://efcl.info/2022/12/15/url-cheatsheet/`; // チャットルームへのリンクを設定
    roomlink.textContent = roomlist[i];
    eachRoom.appendChild(roomlink);

    const editLink = document.createElement('a');
    editLink.href = '../templates/createroom.html'

    const editIcon = document.createElement('img');
    editIcon.src = '../static/img/edit.png'; // 画像パス
    editIcon.alt = 'ルームを編集'; // 代替テキスト
    editIcon.width = 20; // 横サイズ（px）
    editIcon.height = 20; // 縦サイズ（px）
    editLink.appendChild(editIcon);
    eachRoom.appendChild(editLink);

    const deleteIcon = document.createElement('img');
    deleteIcon.src = '../static/img/bin.png'; // 画像パス
    deleteIcon.alt = 'delete'; // 代替テキスト
    deleteIcon.width = 20; // 横サイズ（px）
    deleteIcon.height = 20; // 縦サイズ（px）
    deleteIcon.addEventListener('click', function() {
        const confirmation = confirm (`「${roomlist[i]}」を本当に削除しますか？`);
        if (confirmation) {
        eachRoom.remove();
        console.log(`「${roomlist[i]}」は削除されました。`);
        }
    })
    eachRoom.appendChild(deleteIcon);

    document.getElementById('getChatroom').appendChild(eachRoom);
    }

//掲示板の一覧表示
const bulltinboard = ['勤怠確定8/3まで', '7/20 懇親イベント実施。詳しくはメールをご参照ください。']
          
    for (let i = 0; i < bulltinboard.length; i++) {
    const li = document.createElement('li');
    li.textContent = bulltinboard[i];
    document.getElementById('bulltinboard').appendChild(li).classList.add("bulltinboard");  
    }