# Быстрый старт с МК серии K1921BK VSCode+Platform.io
[PlatformIO]() - Открытая экосистема для IoT разработки.  
Данный репозиторий добавляет поддержку разработки под МК серии K1921BK.  
Используется адаптированный фреймоврк [NIIET k1921vk SDK](https://github.com/kenny5660/framework-k1921vk-sdk), который основан на официальном [SDK от НИИЭТ](https://bitbucket.org/niietcm4/k1921vkx_sdk/src)

## Список поддерживаемых МК:
* К1921ВК01Т
* К1921ВК035
* К1921ВК028

## Найстройка среды разработки
1. [Установка Visual Studio Code](https://code.visualstudio.com/)
2. [Установка PlatformIO](https://docs.platformio.org/en/latest/integration/ide/vscode.html#ide-vscode)
3. После успешной утсановки расширения в левом боковом меню появится эмблема  Platform.io, кликаем туда, затем Open. Откроется окно PIO Home.
4. Создаем новый проект (кнопка New Project),
   *    Name - Название проека
   *    Board - Выбираем используемый контроллер (Сейчас доступны Generic K1921VK01T и Generic K1921VK035)
   *    Framework - используемый фреймоврк для разработки, пока доступен только - NIIET k1921vk SDK 
5. Platform io самостоятельно скачает все требуемые библиотеки, компиляторы, openocd и тд.

Примеры проектов можно увидеть: PIO Home > Platforms > K1921VK > Examples  
Или в [репозитории платформы] (https://github.com/kenny5660/pio_platform_k1921vk/tree/master/examples)
