# OS-scheduling
OS Scheduling Algorithm
## First-Come, First-Served (FCFS) Scheduling
แนวคิด:
- จัดลำดับการทำงานของ process ตามลำดับที่เข้ามาในระบบ (เหมือนคิว FIFO)
- ไม่มีการสลับเปลี่ยน process จนกว่าจะเสร็จ

ข้อดี:
- เข้าใจง่าย และใช้ทรัพยากรต่ำ
- Context Switching ต่ำ

ข้อเสีย:
- เกิด Convoy Effect ถ้า process ที่มาก่อนใช้เวลานาน process ที่ตามมาจะต้องรอนานมาก
- ไม่เหมาะกับระบบที่ต้องการตอบสนองเร็ว

## Round Robin (RR) Scheduling
แนวคิด:
- จัด process แบบหมุนเวียน โดยแต่ละ process จะได้รับเวลาการทำงานตาม Time Quantum
- ถ้า process ยังไม่เสร็จภายใน TQ ก็จะถูกพักและส่งไปต่อท้ายคิว รอรอบถัดไป

ข้อดี:
- ลดปัญหา Convoy Effect
- ทุก process ได้รับโอกาสทำงานเท่าๆกัน
- เหมาะกับระบบ Multitasking

ข้อเสีย:
- มีการ Context Switching บ่อย
- ถ้าเลือก TQ ไม่เหมาะสม (มากเกินไปหรือเล็กเกินไป) อาจส่งผลให้การทำงานไม่มีประสิทธิภาพ