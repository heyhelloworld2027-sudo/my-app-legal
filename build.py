# يولّد الصفحات الثلاث. عدّل المتغيرات أدناه ثم شغّل: python build.py
APP="[Hey Hello Word!]"; APP_EN="[Hey Hello Word!]"
MAIL="[hey.hello.world.2027@gmail.com]"
DATE_AR="1 نوفمبر 2026"; DATE_EN="November 1, 2026"

def page(fname, tab_ar, tab_en, body):
    nav=lambda f,a,e:f'<a href="{f}" class="{"on" if f==fname else ""}"><span data-l="ar">{a}</span><span data-l="en">{e}</span></a>'
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl" data-lang="ar">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{tab_en} | {Hey Hello World!}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script src="lang.js"></script>
</head>
<body><div class="wrap">
<header class="top">
<nav>{nav("index.html","الرئيسية","Home")}{nav("privacy.html","سياسة الخصوصية","Privacy Policy")}{nav("terms.html","الشروط والأحكام","Terms")}</nav>
<div class="lang"><button data-set="ar">العربية</button> <button data-set="en">English</button></div>
</header>
{body}
<footer><span data-l="ar">© {Hey Hello World!} — جميع الحقوق محفوظة.</span><span data-l="en">© {Hey Hello World!} — All rights reserved.</span></footer>
</div></body></html>'''

def sec(ar_t,ar_b,en_t,en_b):
    return f'<h2 data-l="ar">{ar_t}</h2><div data-l="ar">{ar_b}</div><h2 data-l="en">{en_t}</h2><div data-l="en">{en_b}</div>\n'

privacy_head=f'''<h1><span data-l="ar">سياسة الخصوصية</span><span data-l="en">Privacy Policy</span></h1>
<p class="date"><span data-l="ar">آخر تحديث: {DATE_AR}</span><span data-l="en">Last updated: {DATE_EN}</span></p>
<div class="box"><span data-l="ar">توضح هذه السياسة كيف يجمع تطبيق <b>{APP}</b> بياناتك ويستخدمها ويحميها. باستخدامك التطبيق فإنك توافق على ما ورد هنا.</span><span data-l="en">This policy explains how <b>{APP_EN}</b> collects, uses and protects your data. By using the app you agree to it.</span></div>'''

privacy = privacy_head + \
sec("1. البيانات التي نجمعها","""<ul>
<li><b>بيانات الحساب:</b> البريد الإلكتروني، كلمة المرور (تُخزَّن مشفّرة لدى مزوّد المصادقة ولا نراها)، الاسم، والصورة الشخصية.</li>
<li><b>المحتوى الذي تنشئه:</b> الفيديوهات والصور والبثوث المباشرة والتعليقات التي ترفعها.</li>
<li><b>الموقع الجغرافي التقريبي:</b> لأغراض الأمان والتحقق من الدولة/المدينة.</li>
<li><b>بيانات الاستخدام:</b> المدن التي تدخل إليها، عدد المشاهدات، حالة الاتصال (متصل/غير متصل)، وإعدادات اللغة.</li>
<li><b>بيانات الجهاز:</b> نوع الجهاز ونظام التشغيل ومعرّف الإشعارات لإرسال التنبيهات.</li>
</ul>""","1. Data we collect","""<ul>
<li><b>Account data:</b> email, password (stored encrypted by our authentication provider; we cannot see it), name and profile picture.</li>
<li><b>Content you create:</b> videos, images, live streams and comments you upload.</li>
<li><b>Approximate location:</b> used for security and country/city verification.</li>
<li><b>Usage data:</b> cities you open, view counts, online status and language settings.</li>
<li><b>Device data:</b> device type, operating system and notification identifier used to deliver alerts.</li>
</ul>""") + \
sec("2. كيف نستخدم بياناتك","""<ul><li>تشغيل التطبيق وتسجيل الدخول وإدارة حسابك.</li><li>عرض المحتوى والمدن والمشاهدات.</li><li>إرسال الإشعارات (مثل فتح مدينة جديدة).</li><li>حماية التطبيق ومنع الاحتيال والمخالفات وتطبيق الحظر.</li><li>تحسين الأداء وإصلاح الأخطاء.</li></ul><p>لا نبيع بياناتك الشخصية لأي طرف.</p>""",
"2. How we use your data","""<ul><li>To run the app, sign you in and manage your account.</li><li>To display content, cities and view counts.</li><li>To send notifications (e.g. a new city opening).</li><li>To keep the app safe, prevent fraud and enforce bans.</li><li>To improve performance and fix bugs.</li></ul><p>We do not sell your personal data.</p>""") + \
sec("3. الأذونات التي يطلبها التطبيق","""<p>الكاميرا والميكروفون (للتصوير والبث)، الصور/الملفات (لاختيار صورة أو فيديو)، الموقع، والإشعارات. يمكنك إيقاف أي إذن من إعدادات جهازك، وقد تتوقف بعض الميزات عندها.</p>""",
"3. Permissions","""<p>Camera and microphone (recording and live streaming), photos/files (picking media), location, and notifications. You can disable any permission in your device settings; some features may then stop working.</p>""") + \
sec("4. الخدمات الخارجية","""<p>نستخدم مزوّدين موثوقين لتشغيل التطبيق: <b>Supabase</b> (المصادقة وقاعدة البيانات والتخزين)، وخدمات الإشعارات (<b>Firebase Cloud Messaging / OneSignal</b>). لكل منهم سياسة خصوصية خاصة به.</p>""",
"4. Third-party services","""<p>We rely on trusted providers: <b>Supabase</b> (authentication, database and storage) and notification services (<b>Firebase Cloud Messaging / OneSignal</b>). Each has its own privacy policy.</p>""") + \
sec("5. المحتوى العام ومشاركته","""<p>المحتوى الذي تنشره في المدن قد يراه مستخدمون آخرون. لا تنشر معلومات حساسة لا تريد أن تكون عامة.</p>""",
"5. Public content","""<p>Content you publish in cities may be visible to other users. Do not post sensitive information you do not want to be public.</p>""") + \
sec("6. الاحتفاظ بالبيانات وحذفها","""<p>نحتفظ ببياناتك ما دام حسابك نشطاً. لحذف حسابك وبياناتك نهائياً راسلنا على <a href="mailto:%s">%s</a> من البريد المسجَّل به، وسننفّذ الطلب خلال 30 يوماً. قد نحتفظ بسجلات محدودة عند الضرورة القانونية أو الأمنية.</p>"""%(MAIL,MAIL),
"6. Retention and deletion","""<p>We keep your data while your account is active. To permanently delete your account and data, email <a href="mailto:%s">%s</a> from your registered address and we will process it within 30 days. We may keep limited records where legally or security-wise required.</p>"""%(MAIL,MAIL)) + \
sec("7. الأمان","""<p>نستخدم اتصالات مشفّرة (HTTPS) وضوابط وصول وتنقية للمدخلات. لا توجد وسيلة آمنة 100% ولكننا نعمل باستمرار على حماية بياناتك.</p>""",
"7. Security","""<p>We use encrypted connections (HTTPS), access controls and input validation. No method is 100% secure, but we continuously work to protect your data.</p>""") + \
sec("8. الأطفال","""<p>التطبيق غير موجّه لمن هم دون 13 عاماً، ولا نجمع بياناتهم عن علم. إن اكتشفت أن طفلاً سجّل لدينا فراسلنا لحذف الحساب.</p>""",
"8. Children","""<p>The app is not directed to children under 13 and we do not knowingly collect their data. If you believe a child has registered, contact us to delete the account.</p>""") + \
sec("9. حقوقك","""<p>يحق لك طلب الاطلاع على بياناتك أو تصحيحها أو حذفها أو سحب موافقتك، عبر التواصل معنا.</p>""",
"9. Your rights","""<p>You may request access to, correction of or deletion of your data, or withdraw consent, by contacting us.</p>""") + \
sec("10. التغييرات والتواصل","""<p>قد نحدّث هذه السياسة، وسيظهر تاريخ آخر تحديث أعلاه. للتواصل: <a href="mailto:%s">%s</a></p>"""%(MAIL,MAIL),
"10. Changes and contact","""<p>We may update this policy; the date above will change. Contact: <a href="mailto:%s">%s</a></p>"""%(MAIL,MAIL))

terms_head=f'''<h1><span data-l="ar">الشروط والأحكام</span><span data-l="en">Terms &amp; Conditions</span></h1>
<p class="date"><span data-l="ar">آخر تحديث: {DATE_AR}</span><span data-l="en">Last updated: {DATE_EN}</span></p>
<div class="box"><span data-l="ar">باستخدامك تطبيق <b>{APP}</b> أو إنشاء حساب فيه، فإنك توافق على هذه الشروط. إن لم توافق فلا تستخدم التطبيق.</span><span data-l="en">By using <b>{APP_EN}</b> or creating an account you agree to these terms. If you do not agree, do not use the app.</span></div>'''

terms = terms_head + \
sec("1. الأهلية","<p>يجب ألا يقل عمرك عن 13 عاماً، وأن تكون المعلومات التي تقدّمها صحيحة.</p>","1. Eligibility","<p>You must be at least 13 years old and provide accurate information.</p>") + \
sec("2. الحساب","<p>أنت مسؤول عن سرية بيانات دخولك وعن كل نشاط يتم عبر حسابك. أبلغنا فوراً عن أي استخدام غير مصرّح به.</p>","2. Your account","<p>You are responsible for keeping your credentials confidential and for all activity under your account. Tell us immediately about any unauthorized use.</p>") + \
sec("3. السلوك المحظور","""<p>يُمنع:</p><ul><li>نشر محتوى غير قانوني أو عنيف أو جنسي أو مسيء أو يحرّض على الكراهية.</li><li>انتهاك حقوق الآخرين أو حقوق النشر أو انتحال الشخصية.</li><li>محاولة اختراق التطبيق أو تجاوز الحماية أو إساءة استخدام الخدمة.</li><li>رفع برمجيات ضارة أو محتوى مضلل أو بريد مزعج.</li></ul>""",
"3. Prohibited conduct","""<p>You may not:</p><ul><li>Post illegal, violent, sexual, abusive or hateful content.</li><li>Infringe others’ rights or copyrights, or impersonate anyone.</li><li>Attempt to hack the app, bypass protections or abuse the service.</li><li>Upload malware, misleading content or spam.</li></ul>""") + \
sec("4. المحتوى الذي تنشره","<p>تحتفظ بملكية محتواك، وتمنحنا ترخيصاً غير حصري لعرضه وتخزينه ومعالجته داخل التطبيق لتشغيل الخدمة. تضمن أن لديك الحق في نشره. يحق لنا إزالة أي محتوى مخالف دون إشعار.</p>","4. Your content","<p>You keep ownership of your content and grant us a non-exclusive licence to display, store and process it within the app to operate the service. You confirm you have the right to post it. We may remove violating content without notice.</p>") + \
sec("5. الإيقاف والحظر","<p>يحق لنا تعليق حسابك أو حظره نهائياً عند مخالفة هذه الشروط. ويمكنك حذف حسابك في أي وقت بالتواصل معنا.</p>","5. Suspension and bans","<p>We may suspend or permanently ban your account for violating these terms. You may delete your account at any time by contacting us.</p>") + \
sec("6. إخلاء المسؤولية","<p>يُقدَّم التطبيق «كما هو» دون ضمانات بعدم الانقطاع أو الخلو من الأخطاء. ولا نتحمل مسؤولية المحتوى الذي ينشره المستخدمون، ولا أي أضرار غير مباشرة ناتجة عن الاستخدام، إلى أقصى حد يسمح به القانون.</p>","6. Disclaimer","<p>The app is provided “as is” without warranty of uninterrupted or error-free service. We are not responsible for user-posted content or for indirect damages arising from use, to the extent permitted by law.</p>") + \
sec("7. الخصوصية","<p>يخضع جمع بياناتك واستخدامها لـ <a href=\"privacy.html\">سياسة الخصوصية</a>.</p>","7. Privacy","<p>Our collection and use of your data is governed by the <a href=\"privacy.html\">Privacy Policy</a>.</p>") + \
sec("8. التعديلات","<p>قد نعدّل هذه الشروط، واستمرارك في استخدام التطبيق بعد التعديل يعني قبولك لها.</p>","8. Changes","<p>We may modify these terms; continued use after changes means you accept them.</p>") + \
sec("9. التواصل","<p>لأي استفسار: <a href=\"mailto:%s\">%s</a></p>"%(MAIL,MAIL),"9. Contact","<p>Questions: <a href=\"mailto:%s\">%s</a></p>"%(MAIL,MAIL))

index=f'''<h1>{APP}</h1>
<p class="date"><span data-l="ar">المستندات القانونية للتطبيق</span><span data-l="en">Legal documents for the app</span></p>
<div class="cards">
<a href="privacy.html"><b><span data-l="ar">سياسة الخصوصية</span><span data-l="en">Privacy Policy</span></b><span data-l="ar">ما نجمعه من بيانات وكيف نحميها.</span><span data-l="en">What data we collect and how we protect it.</span></a>
<a href="terms.html"><b><span data-l="ar">الشروط والأحكام</span><span data-l="en">Terms &amp; Conditions</span></b><span data-l="ar">قواعد استخدام التطبيق.</span><span data-l="en">Rules for using the app.</span></a>
</div>'''

for f,ta,te,b in [("index.html","الرئيسية","Home",index),("privacy.html","سياسة الخصوصية","Privacy Policy",privacy),("terms.html","الشروط والأحكام","Terms & Conditions",terms)]:
    open(f,"w",encoding="utf-8").write(page(f,ta,te,b))
print("done")
