# de-interlacing
Научно-исследовательская работа: Устранение помех на фотографии

## Структура
- data/ — входные изображения
- denoisers/ — алгоритмы
- metrics/ — PSNR, SSIM
- experiments/ — сценарии запуска

## Запуск
```bash
python experiments/run_batch.py

project/
├── data/ # Оригинальные и зашумлённые изображения
│   ├── noisy/
│   └── original/
├── denoisers/ # Реализации алгоритмов фильтрации
│   ├── gaussian.py
│   ├── median.py
│   └── nl_means.py
├── experiments/ # Сценарии запуска экспериментов
│   ├── add_noise.py
│   ├── evaluate.py
│   ├── plot_metrics.py
│   ├── run_batch.py
│   └── run_single.py
├── metrics/ # Метрики PSNR, SSIM
│   ├── psnr.py
│   └── ssim.py
├── results/ # Результаты экспериментов
│   ├── gaussian/
│   ├── median/
│   ├── nl_means/
│   ├── plots/
│   └── metrics.csv
├── utils/ # Утилиты: добавление шума, загрузка/сохранение изображений
│   ├── io.py
│   ├── noise.py
├── README.md # Документация
└── requirements.txt # Зависимости проекта