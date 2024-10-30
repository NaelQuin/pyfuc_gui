import streamlit as st
from PIL import Image

API_KEYS_FILE = "./.streamlit/apiKeys.txt"
CACHE_PATH = "./.streamlit/cache"

defaultLanguage = "Portuguese"

fa_icons = {
    # Black
    'settingsB': '<i class="fa-solid fa-gear"></i>',
    'folderB': '<i class="fa-solid fa-folder"></i>',
    'editB': '<i class="fa-solid fa-pencil"></i>',
    'fileB': '<i class="fa-solid fa-file-lines"></i>',
    'keyB': '<i class="fa-solid fa-key"></i>',
    'gearsB': '<i class="fa-solid fa-gears"></i>',
    'wordB': '<i class="fa-solid fa-file-word"></i>',
    'pdfB': '<i class="fa-solid fa-file-pdf"></i>',
    'uploadB': '<i class="fa-solid fa-upload"></i>',

    # White
    'settingsW': '<i class="fa-regular fa-gear"></i>',
    'folderW': '<i class="fa-regular fa-folder"></i>',
    'editW': '<i class="fa-light fa-pencil"></i>',
    'fileW': '<i class="fa-solid fa-file-lines"></i>',
    'keyW': '<i class="fa-regular fa-key"></i>',
    'gearsW': '<i class="fa-regular fa-gears"></i>',
    'wordW': '<i class="fa-regular fa-file-word"></i>',
    'pdfW': '<i class="fa-regular fa-file-pdf"></i>',
    'uploadW': '<i class="fa-regular fa-upload"></i>',
}

icons = {
    "favicon": Image.open("./icons/piaget.png"),
    "instructions": ["ℹ️"][0],
    "edit": ["✎", "📝", "✏️"][0],
    "home": Image.open("./icons/house.png"),
    "garbage": Image.open("./icons/garbage.png"),
    "download": Image.open("./icons/download.png"),
    "settings": ["⚙️"][0],
    "upload": Image.open("./icons/upload.png"),
    "sad": ["😔", "😢", "😭", "☹"][2],
    "plus": ["**+**", "Add new key"][1],
    "gpt": ["💭", "🧠", "🖥️", "🛠️", "⚙️"][-2],
    "upload": ["📤", "⬆️"][1],
    "download": ["📥", "💾"][0],
    "revert": ["↩️", "🔄", "🔙", "⬅️"][0]
}

favicon = icons["favicon"]
instructionsIcon = ["ℹ️", icons["instructions"]][0]
editIcon = ["✎", "📝", "✏️", icons["edit"]][0]
plusIcon = ["**+**", "Add new key"][1]
gptIcon = ["🤖", "🧠", "🖥️", "🧰"][3]
settingsIcon = ["⚙️", icons["settings"]][0]

with open(API_KEYS_FILE, "r") as f:
    apiKeys = f.readlines()

abbreviate = {
    "Portuguese": "PT-PT",
    "English": "EN-GB",
    "Spanish": "ES",
    "French": "FR",
    "German": "DE",
    "Chinese": "ZH-hans",
    "Arabic": "AR"
}

_data = {
    'PT-PT': {
        'title': "Pyfuc - Gerador de Ficha de Unidade Curricular",
        'description': "Transforme a criação de fichas de unidades curriculares em uma experiência simples e eficiente com nosso aplicativo inovador. Desenvolvido para atender às necessidades de estudantes, professores e profissionais da educação, nosso aplicativo utiliza a avançada tecnologia do OpenAI GPT para gerar fichas de unidades curriculares personalizadas com base nas suas entradas. Você também pode definir a persona do modelo GPT para combinar com o tom da ficha de unidade curricular. O aplicativo permite que você personalize o prompt para o modelo GPT gerar a ficha de unidade curricular.",
        'api': "Insira a sua chave da API do GPT:",
        'apiNew': "Digite/cole a nova chave da API do GPT:",
        'gptModel': "Selecione o modelo GPT:",
        'persona': "Selecione a persona do GPT:",
        'promptPlaceholder': "Insira seu prompt aqui...",
        'prompt': "Selecione o prompt:",
        'generateResponse': "Gerar Resposta",
        'selectLanguage': "Selecionar idioma:",
        'settings': "Configurações",
        'instructionsTitle': "Instruções",
        'instructions': "1. Insira a sua chave da API do GPT.\n2. Selecione o modelo GPT.\n3. Escolha a persona do GPT.\n4. Insira o prompt.\n5. Clique em 'Gerar Resposta' para gerar a ficha de unidade curricular.",
        'viewResponse': "Ver saída"
    },
    'EN-GB': {
        'title': "Pyfuc - Course Unit Sheet Generator",
        'description': "Transform the creation of course unit sheets into a simple and efficient experience with our innovative app. Developed to meet the needs of students, teachers, and education professionals, our app uses advanced OpenAI GPT technology to generate customized course unit sheets based on your inputs. You can also set the persona of the GPT model to match the tone of the course unit sheet. The app allows you to customize the prompt for the GPT model to generate the course unit sheet.",
        'api': "Enter your GPT API Key:",
        'apiNew': "Enter/paste the new GPT API Key:",
        'gptModel': "Select GPT Model:",
        'persona': "Select the GPT persona:",
        'promptPlaceholder': "Enter your prompt here...",
        'prompt': "Select prompt:",
        'generateResponse': "Generate Response",
        'selectLanguage': "Select language:",
        'settings': "Settings",
        'instructionsTitle': "Instructions",
        'instructions': "1. Enter your GPT API Key.\n2. Select the GPT Model.\n3. Set the GPT persona.\n4. Enter the prompt.\n5. Click on 'Generate Response' to generate the course unit sheet.",
        'viewResponse': "View output"
    },
    'FR': {
        'title': "Pyfuc - Générateur de Fiche d'Unité de Cours",
        'description': "Transformez la création de fiches d'unités de cours en une expérience simple et efficace avec notre application innovante. Développée pour répondre aux besoins des étudiants, des enseignants et des professionnels de l'éducation, notre application utilise la technologie avancée d'OpenAI GPT pour générer des fiches d'unités de cours personnalisées basées sur vos entrées. Vous pouvez également définir la persona du modèle GPT pour correspondre au ton de la fiche d'unité de cours. L'application vous permet de personnaliser le prompt pour que le modèle GPT génère la fiche d'unité de cours.",
        'api': "Entrez votre clé API GPT :",
        'apiNew': "Entrez/collez la nouvelle clé API GPT :",
        'gptModel': "Sélectionnez le modèle GPT :",
        'persona': "Sélectionnez la persona GPT :",
        'promptPlaceholder': "Entrez votre prompt ici...",
        'prompt': "Sélectionnez le prompt :",
        'generateResponse': "Générer la réponse",
        'selectLanguage': "Sélectionner la langue:",
        'settings': "Paramètres",
        'instructionsTitle': "Instructions",
        'instructions': "1. Entrez votre clé API GPT.\n2. Sélectionnez le modèle GPT.\n3. Définissez la persona GPT.\n4. Entrez le prompt.\n5. Cliquez sur 'Générer la réponse' pour générer la fiche d'unité de cours.",
        'viewResponse': "Voir la sortie"
    },
    'AR': {
        'title': "Pyfuc - مولد ورقة الوحدة الدراسية",
        'description': "قم بتحويل إنشاء أوراق الوحدات الدراسية إلى تجربة بسيطة وفعالة مع تطبيقنا المبتكر. تم تطوير تطبيقنا لتلبية احتياجات الطلاب والمعلمين والمهنيين في مجال التعليم، ويستخدم تقنية OpenAI GPT المتقدمة لإنشاء أوراق وحدات دراسية مخصصة بناءً على مدخلاتك. يمكنك أيضًا تحديد شخصية نموذج GPT لتتناسب مع نبرة ورقة الوحدة الدراسية. يتيح لك التطبيق تخصيص الموجه لنموذج GPT لإنشاء ورقة الوحدة الدراسية.",
        'api': "أدخل مفتاح API الخاص بـ GPT:",
        'apiNew': "أدخل/الصق مفتاح API الجديد الخاص بـ GPT:",
        'gptModel': "حدد نموذج GPT:",
        'persona': "اختر شخصية GPT:",
        'promptPlaceholder': "أدخل الموجه الخاص بك هنا...",
        'prompt': "اختر الموجه:",
        'generateResponse': "إنشاء الاستجابة",
        'selectLanguage': "اختر اللغة:",
        'settings': "الإعدادات",
        'instructionsTitle': "التعليمات",
        'instructions': "1. أدخل مفتاح API الخاص بـ GPT.\n2. حدد نموذج GPT.\n3. حدد شخصية GPT.\n4. أدخل الموجه.\n5. انقر على 'إنشاء الاستجابة' لإنشاء ورقة الوحدة الدراسية.",
        'viewResponse': "عرض النتيجة"
    },
    'ES': {
        'title': "Pyfuc - Generador de Ficha de Unidad de Curso",
        'description': "Transforme la creación de fichas de unidades de curso en una experiencia simple y eficiente con nuestra innovadora aplicación. Desarrollada para satisfacer las necesidades de estudiantes, profesores y profesionales de la educación, nuestra aplicación utiliza la avanzada tecnología de OpenAI GPT para generar fichas de unidades de curso personalizadas basadas en sus entradas. También puede establecer la personalidad del modelo GPT para que coincida con el tono de la ficha de unidad de curso. La aplicación le permite personalizar el prompt para que el modelo GPT genere la ficha de unidad de curso.",
        'api': "Ingrese su clave API de GPT:",
        'apiNew': "Ingrese/pegue la nueva clave API de GPT:",
        'gptModel': "Seleccione el modelo GPT:",
        'persona': "Seleccione la personalidad de GPT:",
        'promptPlaceholder': "Ingrese su prompt aquí...",
        'prompt': "Seleccione el prompt:",
        'generateResponse': "Generar Respuesta",
        'selectLanguage': "Seleccionar idioma:",
        'settings': "Configuración",
        'instructionsTitle': "Instrucciones",
        'instructions': "1. Ingrese su clave API de GPT.\n2. Seleccione el modelo GPT.\n3. Establezca la personalidad de GPT.\n4. Ingrese el prompt.\n5. Haga clic en 'Generar Respuesta' para generar la ficha de unidad de curso.",
        'viewResponse': "Ver salida"
    },
    'ZH-hans': {
        'title': "Pyfuc - 课程单元表生成器",
        'description': "通过我们创新的应用程序，将课程单元表的创建转变为简单高效的体验。我们的应用程序专为满足学生、教师和教育专业人士的需求而开发，使用先进的OpenAI GPT技术根据您的输入生成定制的课程单元表。您还可以设置GPT模型的角色以匹配课程单元表的语气。该应用程序允许您自定义GPT模型生成课程单元表的提示。",
        'api': "输入您的GPT API密钥：",
        'apiNew': "输入/粘贴新的GPT API密钥：",
        'gptModel': "选择GPT模型：",
        'persona': "选择GPT角色：",
        'promptPlaceholder': "在此输入您的提示...",
        'prompt': "选择提示：",
        'generateResponse': "生成响应",
        'selectLanguage': "选择语言:",
        'settings': "设置",
        'instructionsTitle': "说明",
        'instructions': "1. 输入您的GPT API密钥。\n2. 选择GPT模型。\n3. 设置GPT角色。\n4. 输入提示。\n5. 点击'生成响应'以生成课程单元表。",
        'viewResponse': "查看输出"
    },
    'DE': {
        'title': "Pyfuc - Kurseinheitsblatt-Generator",
        'description': "Verwandeln Sie die Erstellung von Kurseinheitsblättern in eine einfache und effiziente Erfahrung mit unserer innovativen App. Entwickelt, um den Bedürfnissen von Studenten, Lehrern und Bildungsfachleuten gerecht zu werden, verwendet unsere App fortschrittliche OpenAI GPT-Technologie, um personalisierte Kurseinheitsblätter basierend auf Ihren Eingaben zu generieren. Sie können auch die Persona des GPT-Modells festlegen, um den Ton des Kurseinheitsblatts anzupassen. Die App ermöglicht es Ihnen, den Prompt für das GPT-Modell zur Generierung des Kurseinheitsblatts anzupassen.",
        'api': "Geben Sie Ihren GPT-API-Schlüssel ein:",
        'apiNew': "Geben Sie den neuen GPT-API-Schlüssel ein/fügen Sie ihn ein:",
        'gptModel': "Wählen Sie das GPT-Modell aus:",
        'persona': "Wählen Sie die GPT-Persona aus:",
        'promptPlaceholder': "Geben Sie hier Ihren Prompt ein...",
        'prompt': "Wählen Sie den Prompt aus:",
        'generateResponse': "Antwort generieren",
        'selectLanguage': "Sprache auswählen:",
        'settings': "Einstellungen",
        'instructionsTitle': "Anweisungen",
        'instructions': "1. Geben Sie Ihren GPT-API-Schlüssel ein.\n2. Wählen Sie das GPT-Modell aus.\n3. Legen Sie die GPT-Persona fest.\n4. Geben Sie den Prompt ein.\n5. Klicken Sie auf 'Antwort generieren', um das Kurseinheitsblatt zu erstellen.",
        'viewResponse': "Ausgabe anzeigen"
    }
}

_personas = {
    "EN-GB": [
        "Senior polytechnic director",
        "Senior academic director",
        "Senior director of a higher technical course"
    ],

    "PT-PT": [
        "Diretor sénior de politécnico",
        "Diretor académico sénior",
        "Diretor sénior de um curso técnico superior"
    ],
    "FR": [
        "Directeur principal d'un institut polytechnique",
        "Directeur académique principal",
        "Directeur principal d'un cours technique supérieur"
    ],
    "AR": [
        "مدير كلية تقنية عليا",
        "مدير أكاديمي كبير",
        "مدير كبير لدورة تقنية عليا"
    ],
    "ES": [
        "Director senior de politécnico",
        "Director académico senior",
        "Director senior de un curso técnico superior"
    ],
    "ZH-hans": [
        "高级理工学院主任",
        "高级学术主任",
        "高级技术课程主任"
    ],
    "DE": [
        "Leitender Direktor einer Fachhochschule",
        "Leitender akademischer Direktor",
        "Leitender Direktor eines höheren technischen Kurses"
    ]
}

_prompts = {
    "EN-GB": [
        "FUC from syllabus",
        "Bibliography from syllabus",
        "Intended learning outcomes from syllabus",
        "Teaching methodologies and assessments from syllabus",
        "Other"
    ],

    "PT-PT": [
        "FUC a partir do programa",
        "Bibliografia a partir do programa",
        "Objetivos de aprendizagem a partir do programa",
        "Metologias de ensino e avaliações a partir do programa",
        "Outro"
    ],
    "FR": [
        "FUC à partir du programme",
        "Bibliographie à partir du programme",
        "Objectifs d'apprentissage à partir du programme",
        "Méthodologies d'enseignement et évaluations à partir du programme",
        "Autre"
    ],
    "AR": [
        "FUC من المنهج الدراسي",
        "المراجع من المنهج الدراسي",
        "نتائج التعلم المقصودة من المنهج الدراسي",
        "منهجيات التدريس والتقييمات من المنهج الدراسي",
        "آخر"
    ],
    "ES": [
        "FUC del programa",
        "Bibliografía del programa",
        "Resultados de aprendizaje previstos del programa",
        "Metodologías de enseñanza y evaluaciones del programa",
        "Otro"
    ],
    "ZH-hans": [
        "教学大纲中的FUC",
        "教学大纲中的参考书目",
        "教学大纲中的预期学习成果",
        "教学大纲中的教学方法和评估",
        "其他"
    ],
    "DE": [
        "FUC aus dem Lehrplan",
        "Literaturverzeichnis aus dem Lehrplan",
        "Beabsichtigte Lernergebnisse aus dem Lehrplan",
        "Lehrmethoden und Bewertungen aus dem Lehrplan",
        "Andere"
    ]
}

gptModels = [
    "gpt-4-turbo",
    "gpt-4-turbo-2024-04-09",
    "gpt-4",
    "gpt-4o",
    "gpt-4o-2024-08-06",
    "gpt-4o-2024-05-13",
    "gpt-4o-mini",
    "gpt-4o-mini-2024-07-18",
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k"
]

languages = sorted([
    "Portuguese",
    "English",
    "German",
    "French",
    "Arabic",
    "Spanish",
    "Chinese",
])

defaultData = {
    "generated": False,
    "icons": icons,
    "fa_icons": fa_icons,
    "localVars": {
        "data": _data[abbreviate[defaultLanguage]],
        "language": defaultLanguage,
        "languageAbbrev": abbreviate[defaultLanguage],
    },
    "dicts": {
        "_data": _data,
        "abbreviate": abbreviate,
    },
    "lists": {
        "languages": languages,
        "apiKeys": apiKeys,
        "gptModels": gptModels,
        "_personas": _personas,
    },
}

# --------------------------
# Storing default parameters
# --------------------------
if not any(st.session_state):
    st.session_state.update(defaultData)
