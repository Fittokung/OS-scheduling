def main():
    # รับจำนวน process จากผู้ใช้
    n = int(input("Enter number of process: "))
    # สร้างเมทริกซ์สำหรับเก็บข้อมูล Process Id, burst time, Average Waiting Time และ Average Turn Around Time
    A = [[0 for j in range(4)] for i in range(100)]
    total, avg_wt, avg_tat = 0, 0, 0

    # รับค่า burst time ของแต่ละ process
    print("Enter burst time:")
    for i in range(n):  # รับค่า burst time และกำหนด Process Id
        A[i][1] = int(input(f"P{i+1}: "))
        A[i][0] = i + 1

    # จัดเรียง process ตามค่า burst time
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if A[j][1] < A[index][1]:
                index = j
        # สลับค่า burst time และ Process Id
        temp = A[i][1]
        A[i][1] = A[index][1]
        A[index][1] = temp
        temp = A[i][0]
        A[i][0] = A[index][0]
        A[index][0] = temp

    # คำนวณ Waiting Time
    A[0][2] = 0  # WT ของ process แรก = 0
    for i in range(1, n):
        A[i][2] = 0
        for j in range(i):
            A[i][2] += A[j][1]  # รวม burst time ของ process ก่อนหน้า
        total += A[i][2]  # รวมค่า WT ทั้งหมด

    avg_wt = total / n  # คำนวณค่าเฉลี่ย Waiting Time
    total = 0

    # คำนวณ Turn Around Time และแสดงผลข้อมูล
    print("P     BT     WT     TAT")
    for i in range(n):
        A[i][3] = A[i][1] + A[i][2]  # TAT = BT + WT
        total += A[i][3]  # รวมค่า TAT ทั้งหมด
        print(f"P{A[i][0]}     {A[i][1]}     {A[i][2]}      {A[i][3]}")

    avg_tat = total / n  # คำนวณค่าเฉลี่ย Turn Around Time
    print(f"Average Waiting Time= {avg_wt}")
    print(f"Average Turnaround Time= {avg_tat}")


if __name__ == "__main__":
    main()
