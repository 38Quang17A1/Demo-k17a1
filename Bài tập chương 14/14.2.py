#1.việc nhập dữ liệu kết thúc bình thường (không exception) khi người dùng nhập vào số 0

def so_duong():
 
  numbers = []
  while True:
    number = int(input("Nhập số nguyên dương: "))
    if number == 0:
      break
    numbers.append(number)

  return numbers


numbers = so_duong()
print("Các số nguyên dương đã nhập:", numbers)

#2.phát sinh  exception và thông báo lỗi "Lỗi số âm!!!" khi người dùng nhập vào một số âm
def so_nguyen_duong():

  numbers = []
  while True:
    number = input("Nhập số nguyên dương: ")
    try:
      number = int(number)
      if number < 0:
        raise ValueError("Lỗi số âm!!!")
      numbers.append(number)
    except ValueError:
      print("Lỗi!!!")
      break
  return numbers


numbers = so_nguyen_duong()
print(numbers)

#3.phát sinh  exception và thông báo lỗi "Lỗi nhập số!!!" khi người dùng nhập một chuỗi không phải số nguyên 
def so_nhap_loi():

  numbers = []
  while True:
    number = input("Nhập số nguyên dương tiếp theo: ")
    try:
      numbers.append(int(number))
    except ValueError:
      print("Lỗi nhập số!!!")
    else:
      break
  return numbers


numbers = so_nhap_loi()

#4.phát sinh  exception và thông báo lỗi "Lỗi nhập lặp lại!!!" khi người dùng nhập vào 4 số nguyên dương liên tiếp giống nhau
def so_lap_lai():

  numbers = []
  count = 0
  while True:
    number = input("Nhập số nguyên dương: ")
    try:
      number = int(number)
      if number < 1:
        raise ValueError("Số nhập không hợp lệ")
    except ValueError:
      print("Số nhập không hợp lệ")
      continue

    numbers.append(number)

    if number == numbers[-1]:
      count += 1
    else:
      count = 1

    if count == 4:
      raise Exception("Lỗi nhập lặp lại!!!")
    return numbers


if __name__ == "__main__":
  try:
    numbers = so_lap_lai()
    print("Các số nguyên dương đã nhập:", numbers)
  except Exception as e:
    print(e)


#phát sinh lỗi exception và thông báo lỗi "Lỗi nhập chẵn!!!" khi người dùng  nhập vào 5 số chẵn liên tiếp
    
def input_numbers():
  """
  Nhập các số nguyên dương từ người dùng

  Returns:
    List các số nguyên dương đã nhập
  """

  numbers = []
  count = 0
  while True:
    number = input("Nhập số nguyên dương: ")
    try:
      number = int(number)
      if number < 1:
        raise ValueError("Số nhập không hợp lệ")
    except ValueError:
      print("Số nhập không hợp lệ")
      continue

    numbers.append(number)

    if number % 2 == 0:
      count += 1
    else:
      count = 0

    if count == 5:
      raise Exception("Lỗi nhập chẵn!!!")

  return numbers


if __name__ == "__main__":
  try:
    numbers = input_numbers()
    print("Các số nguyên dương đã nhập:", numbers)
  except Exception as e:
    print(e)


#6.sau khi phát hiện exception, xử lí và thông báo, chương trình lại hoạt động bình thường

def loi_lap_chan():

  numbers = []
  while True:
    number = input("Nhập số nguyên dương: ")
    try:
      number = int(number)
      if number < 1:
        raise ValueError("Số nhập không hợp lệ")
    except ValueError:
      print("Số nhập không hợp lệ")
      continue

    numbers.append(number)

    if len(numbers) >= 4 and numbers[-4:] == numbers[-1:]:
      print("Lỗi nhập lặp lại!!!")
      continue

    return numbers


if __name__ == "__main__":
  while True:
    try:
      numbers = loi_lap_chan()
      print("Các số nguyên dương đã nhập:", numbers)
      break
    except Exception as e:
      print(e)