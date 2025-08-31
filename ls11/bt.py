san_pham = ['a' , 'b' , 'c']
gio_hang = []
# 1 Hiển thị sản phẩm
def hien_thi_san_pham(san_pham):
    for index in range(len(san_pham)):
        print(f"{index + 1}: {san_pham[index]}")

hien_thi_san_pham(san_pham)
# 2 xem giỏ hàng
def xem_gio_hang(gio_hang):
    # khi giỏ hàng rỗng 
    if not gio_hang:
        print("Chưa có sản phẩm trong giỏ hàng.")
    else:
        print("Mặt hàng của bạn bao gồm:")
        for index in range(len(gio_hang)):
            print(f"{index + 1}: {gio_hang[index]}")

# Gọi hàm xem giỏ hàng
xem_gio_hang(gio_hang)
# 3 thêm sp vào dỏ hàng
def them_vao_gio(san_pham , gio_hang):
    print("Danh sách sản phẩm là: ")
    hien_thi_san_pham(san_pham)
    # Tạo biến số lưu trữ vị trí sản phẩm
    item_index = int(input("Nhập sản phẩm bạn muốn thêm vào : ")- 1)
    if item_index >= 0 and item_index < len(san_pham):
        selected_item = san_pham(item_index)
        gio_hang.append(selected_item)
        print( f"{selected_item} đã được thêm vào giỏ hàng")
    else:
        print("Sản phẩm không hợp lệ : ")
them_vao_gio(san_pham , gio_hang)
# 4 xóa sản phẩm ra khỏi giỏ
def xoa_gio_hang(gio_hang):
    if not gio_hang:
        print("Giỏ hàng trống : ")
    else:
        print("Các sản phẩm có trong giỏ hàng là : ")
        xem_gio_hang(gio_hang)
        item_index = int(input("Nhập vị trí sản phẩm bạn muốn xóa : ")- 1)
        if item_index >= 0 and item_index < len(gio_hang):
            delete_item = gio_hang.pop(item_index)
            print(f"{delete_item} đã được đưa lại cửa hàng : ")
        else:
            print("Không hợp lệ : ")
xoa_gio_hang(gio_hang)
