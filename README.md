<div dir=rtl align="justify">
<h1 align="center">غنی‌سازی متن به کمک شعر، غزل، نقل‌قول و حدیث</h1>
<h3 align="center">اعضای تیم: مهدی سعیدی، فرانک کریمی، محمدرضا کمالی، آرمان مظلوم‌زاده</h3>
<h2>تعریف مساله</h2>
<b>ورودی</b>
<p>یک پرس‌وجوی به زبان فارسی که قرار است با محتوای چندزبانه غنی شود.</p>
<b>خروجی</b>
<p>تجمیع نتایج روش‌های مختلف تعیین شباهت که پرس‌و‌جوی ورودی را با محتوای مناسب (شعر، غزل، نقل‌قول و حدیث) که از نظر معنایی مرتبط هستند، غنی می‌کند.
</p>
<b>اهمیت و کاربرد</b>
<p>
این روش با به‌کارگیری مدل‌های مختلف برای
تعیین موارد مرتبط به ورودی به صورت چندزبانه مانند Weighted TF-IDF، LaBSE و FastText Multilingual، سعی
در غنی‌کردن پرس‌وجوی ورودی دارد. تجمیع نتایج این روش‌ها باعث می‌شود که هم خروجی پوشاتری بدست آید
و هم در نهایت با انجام ارزیابی مشخص شود که کدام روش نقش بیشتری در خروجی نهایی داشته است.
بنابراین می‌توان گفت اهمیت اصلی این روش،‌ ایجاد یک مجموعه داده‌ی برچسب‌گذاری‌شده
به همراه ارزیابی بر روی روش‌های پایه‌ای گفته‌شده است که امکان مقایسه‌ی آن‌ها را در چارچوبی علمی ممکن کرده است.

</p>
<h2>روش</h2>
<b>داده و تقسیم‌بندی</b>
<p>
مجموعه‌داده‌های گنجور به زبان فارسی شامل چندین شعر و غزل، مجموعه‌داده‌ی Goodreads به زبان انگلیسی
با ۲۵۰۸ نقل‌قول از نویسندگان سرشناس و مجموعه‌داده‌های نهج‌البلاغه به زبان عربی شامل ۴۸۰ حکمت.
با توجه به اینکه ارزیابی supervised است این داده‌ها تماما به عنوان ورودی به این روش داده می‌شوند.
</p>
<b>روش و داده ارزیابی</b>
<p>
از طریق تعیین relevance score به صورت supervised به این شکل که به ازای هر جمله‌ی پرس‌وجو،
از هر روش ۱۰ قطعه‌ی غنی‌کننده دریافت می‌شود و بنابراین برای هر ورودی روی هم چندین قطعه خواهیم داشت.
سپس به ازای هر جفت پرس‌وجو و هر قطعه‌ی غنی‌کننده‌ی آن، دو نفر عددی بین ۱- و ۱ به آن اختصاص می‌دهند 
و نهایتا امتیاز نهایی با توافق بین آن‌ها تعیین می‌شود. سپس از روش‌هایی مانند Fleiss' kappa صحت امتیازدهی مشخص می‌شود. 
در آخر روش‌های مختلف بر حسب اینکه در مجموع چه امتیازهایی گرفته‌اند رتبه‌بندی می‌شوند. داده‌ی ارزیابی نیز داده‌ای است که به شکل supervised امتیازدهی شده است.
</p>
<b>مدل‌های پایه</b>
<p dir=rtl>Weighted TF-IDF، LaBSE و FastText Multilingual.</p>
<b>مدل‌های اصلی</b>
<p>تجمیع مدل‌های پایه.</p>
</div>