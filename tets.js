//KHỞI TẠO CÁC BIẾN CẦN THIẾT 

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let pnt = []; // points: lưu điểm người dùng chọn 
let md = ""; //mode: chế độ vẽ


//CÁC HÀM DÙNG ĐỂ VẼ HÌNH HỌC 

// Hàm vẽ đường thẳng theo thuật toán Mid-point
function draw_line(p1, p2) {
    let x1 = p1.x, y1 = p1.y, x2 = p2.x, y2 = p2.y;
    let Dx = Math.abs(x2 - x1); //chêch lệch theo x
    let Dy = Math.abs(y2 - y1); //chêch lệch theo y 
    let sx = (x1 < x2) ? 1 : -1; //hướng đi theo trục x 
    let sy = (y1 < y2) ? 1 : -1; //hướng đi theo trục y
    let err = Dx - Dy; //sai số 


    //vòng lặp để vẽ điểm trên đường thẳng 
    while (true) {
        ctx.fillRect(x1, y1, 1, 1); // Vẽ điểm pixel

        //kiểm tra xem đã đến điểm cuối chưa 
        //nếu đã đến điểm cuối cùng thì dừng 
        if (x1 === x2 && y1 === y2) break;

        let e2 = 2 * err;
        if (e2 > -Dy) {
            err -= Dy; //điều chỉnh sai số
            x1 += sx;  //di chuyển theo trục x
        }
        if (e2 < Dx) {
            err += Dx; //điều chỉnh sai số
            y1 += sy; //di chuyển theo trục y
        }
    }
}

// Hàm vẽ Ellipse theo thuật toán Mid-point
function draw_ellipse(cx, cy, rx, ry) {
    let rx2 = rx * rx;
    let ry2 = ry * ry;
    let x = 0, y = ry; //Điểm bắt đầu là (0, ry)
    let p = ry2 - rx2 * ry + rx2 / 4; //sai số ban đầu 

    // Vẽ từ (0, B) -> (A, 0)
    while ((2 * ry2 * x) < (2 * rx2 * y)) {
        plot_ellipse_points(cx, cy, x, y); //vẽ các điểm đối xứng 
        if (p < 0) {
            p += 2 * ry2 * x + ry2; //điều chỉnh sai số
        } else {
            p += 2 * ry2 * x - 2 * rx2 * y + ry2; //điều chỉnh sai số 
            y--;
        }
        x++;
    }

    // vẽ phần còn lại
    p = ry2 * (x + 0.5) * (x + 0.5) + rx2 * (y - 1) * (y - 1) - rx2 * ry2;
    while (y >= 0) {
        plot_ellipse_points(cx, cy, x, y);
        if (p > 0) {
            p -= 2 * rx2 * y - rx2;
        } else {
            p += 2 * ry2 * x - 2 * rx2 * y + rx2;
            x++;
        }
        y--;
    }
}

// Hàm vẽ các điểm đối xứng trên ellipse
function plot_ellipse_points(cx, cy, x, y) {
    ctx.fillRect(cx + x, cy + y, 1, 1); //phần tư thứ 1
    ctx.fillRect(cx - x, cy + y, 1, 1); //phần tư thứ 2
    ctx.fillRect(cx + x, cy - y, 1, 1); //phần tư thứ 3
    ctx.fillRect(cx - x, cy - y, 1, 1); //phần tư thứ 4
}

// Hàm vẽ Parabol theo thuật toán (đỉnh ở tọa độ (vx, vy))
function draw_parabol(vx, vy, p) {
    for (let x = 0; x < 200; x++) {
        let y = Math.sqrt(2 * p * x); //tính y bằng phương trình parabol 
        ctx.fillRect(vx + x, vy + y, 1, 1);
        ctx.fillRect(vx + x, vy - y, 1, 1);
    }
}

// Hàm vẽ Hyperbol theo thuật toán (đỉnh ở tọa độ (hx, hy))
function draw_hyperbol(hx, hy, a, b) {
    for (let x = 0; x < 200; x++) {
        let y = Math.sqrt((x * x / (a * a) - 1) * b * b);
        if (!isNaN(y)) { //kiểm tra xem y có hợp lệ hay không
            ctx.fillRect(hx + x, hy + y, 1, 1); //góc phần tư thứ 1
            ctx.fillRect(hx - x, hy + y, 1, 1); //góc phần tư thứ 2
            ctx.fillRect(hx - x, hy - y, 1, 1); //góc phần tư thứ 3
            ctx.fillRect(hx + x, hy - y, 1, 1); //góc phần tư thứ 4
        }
    }
}


// XỬ LÝ SỰ KIỆN CLICK CHUỘT VÀ CHỌN CHẾ ĐỘ VẼ CỦA NGƯỜI DÙNG 

//chọn chế độ vẽ 
function chooseMode(choosenMode) {
    md = choosenMode;
    pnt = [];
}

//thêm sự kiện nhấn chuột khi người dùng chọn điểm 
canvas.addEventListener('mousedown', (event) => {

    //tính toán tọa độ chuột 
    let rect = canvas.getBoundingClientRect();
    let x = event.clientX - rect.left;
    let y = event.clientY - rect.top;

    //lưu tọa độ điểm vào mảng points
    pnt.push({ x, y });

    //xử lý khi người dùng đã chọn điểm để vẽ 
    if (md === "line" && pnt.length === 2) {
        draw_line(pnt[0], pnt[1]);
        pnt = []; //reset lại mảng sau khi vẽ xong
    } else if (md === "ellipse" && pnt.length === 1) {
        let rx = parseInt(prompt("Nhập bán kính ngang:"));
        let ry = parseInt(prompt("Nhập bán kính dọc:"));
        draw_ellipse(pnt[0].x, pnt[0].y, rx, ry);
        pnt = []; //reset lại mảng sau khi vẽ xong
    } else if (md === "parabola" && pnt.length === 1) {
        let p = parseInt(prompt("Nhập tiêu cự (p):"));
        draw_parabol(pnt[0].x, pnt[0].y, p);
        pnt = []; //reset lại mảng sau khi vẽ xong
    } else if (md === "hyperbola" && pnt.length === 1) {
        let a = parseInt(prompt("Nhập bán trục thực (a):"));
        let b = parseInt(prompt("Nhập bán trục ảo (b):"));
        draw_hyperbol(pnt[0].x, pnt[0].y, a, b);
        pnt = [];
    }
});