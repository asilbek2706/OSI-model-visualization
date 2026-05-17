# OSI Modeli Qatlamlari Vizualizatsiya Qurilmasi

## Loyiha haqida
OSI (Open Systems Interconnection) modeli vizualizatsiya qurilmasi - bu kompyuter tarmoqlarining 7 qatlamli modelini o'rganish uchun mo'ljallangan akademik darajadagi interaktiv dastur. Ushbu dastur ma'lumotlarning bir qurilmadan ikkinchisiga o'tish jarayonini (enkapsulyatsiya va dekapsulyatsiya) vizual tarzda ko'rsatib beradi. Dastur talabalar va tarmoq muhandislari uchun nazariy bilimlarni amaliy ko'rinishda tushunishga yordam beradi.

## Asosiy Imkoniyatlar
- **To'liq 7-qatlamli Vizualizatsiya**: OSI modelining barcha qatlamlari (Application, Presentation, Session, Transport, Network, Data Link, Physical) uchun alohida ko'rinish.
- **Real-vaqtli Animatsiya**: Ma'lumotlar paketining qatlamlar bo'ylab harakati va jismoniy muhit (Physical Medium) orqali o'tishi koordinatali animatsiyalar orqali ko'rsatiladi.
- **Enkapsulyatsiya va Dekapsulyatsiya**: Har bir qatlamda ma'lumotga sarlavhalar (headers) qo'shilishi va ularning olib tashlanishi jarayonini real vaqtda kuzatish.
- **Interaktiv Ta'lim Paneli**: Har bir qatlamning vazifasi, undagi PDU (Protocol Data Unit) turlari (Data, Segment, Packet, Frame, Bit) haqida batafsil ma'lumot beruvchi panel.
- **Boshqaruv Tizimi**: Simulyatsiyani to'xtatish (Pause), davom ettirish (Resume), qayta ishga tushirish (Reset) va tezlikni sozlash imkoniyatlari.
- **Zamonaviy GUI**: CustomTkinter kutubxonasi yordamida yaratilgan zamonaviy va foydalanish uchun qulay interfeys.

## Ishlatilgan Texnologiyalar
- **Python 3.x**: Dasturning asosiy mantiqi va arxitekturasi uchun.
- **CustomTkinter**: Zamonaviy va chiroyli foydalanuvchi interfeysi (GUI) yaratish uchun.
- **Tkinter**: Animatsiyalar va grafik elementlar bilan ishlash uchun.
- **Threading va Asinxron Timing**: Simulyatsiya jarayonida interfeys qotib qolmasligini ta'minlash uchun.

## O'rnatish
1. Loyihani yuklab oling:
   ```bash
   git clone https://github.com/your-username/osi-visualization-tool.git
   cd osi-visualization-tool
   ```
2. Virtual muhit yarating (tavsiya etiladi):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows uchun: venv\Scripts\activate
   ```
3. Zarur kutubxonalarni o'rnating:
   ```bash
   pip install -r requirements.txt
   ```

## Ishga tushirish
Dasturni ishga tushirish uchun quyidagi buyruqni bajaring:
```bash
python main.py
```

## OSI Modeli va Ishlash Prinsipi

### 1. Maqsad va Ahamiyati
OSI modeli zamonaviy telekommunikatsiya va kompyuter tarmoqlarining asosi hisoblanadi. ISO tomonidan 1980-yillarda ishlab chiqilgan ushbu model aloqa tizimini etti mantiqiy qatlamga ajratadi. Ushbu vizualizatsiya qurilmasining maqsadi - darsliklardagi murakkab va mavhum nazariyani jonli, interaktiv va tushunarli animatsiyaga aylantirishdir.

### 2. Enkapsulyatsiya (Encapsulation)
Enkapsulyatsiya - bu ma'lumotlarning yuqori qatlamdan pastki qatlamga o'tishida unga har bir qatlamga xos bo'lgan sarlavhalar (headers) qo'shilishi jarayonidir.
- **Jarayon**: Ma'lumot Application qatlamidan Physical qatlamiga qarab harakatlanadi.
- **Sarlavhalar**: Masalan, Transport qatlamida portlar haqida ma'lumot beruvchi TCP sarlavhasi, Network qatlamida esa manzilni belgilovchi IP sarlavhasi qo'shiladi.
- **PDU turlari**: Data -> Segment -> Packet -> Frame -> Bit.

### 3. Dekapsulyatsiya (Decapsulation)
Bu enkapsulyatsiyaning teskari jarayoni bo'lib, qabul qiluvchi tomonda sodir bo'ladi.
- **Jarayon**: Ma'lumot Physical qatlamidan Application qatlamiga qarab yuqoriga ko'tariladi.
- **Sarlavhalarni ajratish**: Har bir qatlam o'ziga tegishli sarlavhani o'qiydi, tekshiradi va keyin uni olib tashlaydi.
- **Natija**: Eng yuqori qatlamda qabul qiluvchi dastur faqat asl ma'lumotni (payload) qabul qiladi.

## Kod Namunalari

### Paketlarni Enkapsulyatsiya qilish mantiqi (`packet.py`)
Quyidagi kodda ma'lumotga qanday qilib sarlavha qo'shilishi ko'rsatilgan:
```python
def encapsulate(self, layer_name):
    """Qatlam uchun sarlavha qo'shish."""
    header = f"[{layer_name}_Header]"
    self.headers.append(header)
    self.payload = f"{header} {self.payload}"
    return self.payload
```

### Simulyatsiya holatlarini boshqarish (`animations.py`)
Simulyatsiya 15 ta bosqichdan iborat bo'lib, quyidagi mantiq orqali boshqariladi:
```python
def run_loop(self):
    if not self.is_running or self.is_paused:
        return

    if self.current_step < self.total_steps:
        # Navbatdagi bosqichni UI ga yuborish
        self.update_callback(self.current_step, "Running")
        self.current_step += 1
    else:
        self.is_running = False
        self.update_callback(self.current_step, "Finished")
```

## Loyiha Strukturasi
- `main.py`: Dasturning asosi, foydalanuvchi interfeysi (GUI) va simulyatsiya boshqaruvi.
- `packet.py`: Ma'lumotlar paketini boshqarish, enkapsulyatsiya va dekapsulyatsiya algoritmlari.
- `layers.py`: OSI qatlamlari haqidagi ma'lumotlar (nomi, vazifasi, PDU turi) saqlanadigan fayl.
- `animations.py`: Simulyatsiya holatlarini (state machine) va vaqtni boshqarish.
- `utils.py`: Rang palitrasini, oynaning o'lchamlari va konstantalarni belgilash.
- `requirements.txt`: Loyiha uchun zarur bo'lgan tashqi kutubxonalar ro'yxati.

## Xulosa
Ushbu OSI vizualizatsiya qurilmasi ta'lim samaradorligini oshirish uchun yaratilgan. U orqali "ko'rinmas" tarmoq jarayonlarini ko'rish va tushunish imkoniyati mavjud. Dastur kodi modulli tuzilishga ega bo'lib, uni kelajakda kengaytirish yoki boshqa protokollarni (masalan, IPv6 yoki ARP) qo'shish oson.

---
