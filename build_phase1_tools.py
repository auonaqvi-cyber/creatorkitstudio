import os, json

TOOLS_PHASE1 = [
    {
        "dir": "image-resizer",
        "canonical": "https://www.creatorkitstudio.pro/tools/image-resizer/",
        "title": "Free Online Image Resizer – Resize JPG, PNG & WebP | CreatorKit Studio",
        "meta_desc": "Resize, scale, and compress images directly in your browser using HTML5 Canvas. YouTube thumbnail (1280x720), Instagram, and Twitter presets. Zero server uploads.",
        "keywords": "free online image resizer, resize image online, resize JPG, resize PNG, resize WebP, browser-based image resizer, client-side image resizing, youtube thumbnail resizer",
        "h1": "Free Online Image Resizer",
        "badge": "Free Online Image Resizer",
        "summary": "Resize, scale, and convert image files directly in your browser using HTML5 Canvas. Includes one-click aspect ratio presets for YouTube thumbnails (1280×720), Instagram square (1080×1080), Story/Reels (1080×1920), and Twitter graphics. Fast, 100% private, with zero server uploads.",
        "icon": "fa-image",
        "color": "purple",
        "custom_ui": """
            <!-- Image Resizer Interactive Workspace -->
            <div class="space-y-6">
                <!-- Dropzone Area -->
                <div id="dropzone" class="border-2 border-dashed border-slate-300 dark:border-dark-border rounded-2xl p-8 text-center cursor-pointer hover:border-purple-500 transition-colors bg-slate-50/50 dark:bg-slate-900/40">
                    <input type="file" id="imageInput" accept="image/*" class="hidden">
                    <div class="space-y-3 pointer-events-none">
                        <div class="w-14 h-14 rounded-2xl bg-purple-50 dark:bg-purple-950/60 text-purple-600 dark:text-purple-400 flex items-center justify-center text-2xl mx-auto">
                            <i class="fa-solid fa-cloud-arrow-up"></i>
                        </div>
                        <div>
                            <span class="text-sm font-bold text-slate-800 dark:text-slate-100">Click to upload or drag and drop an image</span>
                            <span class="text-xs text-slate-500 dark:text-slate-400 block mt-1">Supports PNG, JPG, WebP, GIF, SVG (100% Local Browser Memory)</span>
                        </div>
                    </div>
                </div>

                <!-- Resizer Controls (Hidden until file selected) -->
                <div id="controlsArea" class="hidden space-y-6">
                    <!-- Presets Strip -->
                    <div class="space-y-2">
                        <span class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Social Media Presets:</span>
                        <div class="flex flex-wrap gap-2">
                            <button type="button" class="preset-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 hover:bg-purple-600 hover:text-white transition" data-w="1280" data-h="720">
                                <i class="fa-brands fa-youtube text-red-500"></i> YouTube (1280×720)
                            </button>
                            <button type="button" class="preset-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 hover:bg-purple-600 hover:text-white transition" data-w="1080" data-h="1080">
                                <i class="fa-brands fa-instagram text-pink-500"></i> IG Square (1080×1080)
                            </button>
                            <button type="button" class="preset-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 hover:bg-purple-600 hover:text-white transition" data-w="1080" data-h="1920">
                                <i class="fa-brands fa-tiktok text-cyan-400"></i> Reel/Story (1080×1920)
                            </button>
                            <button type="button" class="preset-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 hover:bg-purple-600 hover:text-white transition" data-w="1200" data-h="675">
                                <i class="fa-brands fa-x-twitter"></i> Twitter/X (1200×675)
                            </button>
                        </div>
                    </div>

                    <!-- Custom Dimension Controls -->
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <div>
                            <label for="widthInput" class="block text-xs font-semibold text-slate-600 dark:text-slate-400 mb-1">Width (px)</label>
                            <input type="number" id="widthInput" class="w-full p-2.5 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl font-mono text-slate-900 dark:text-slate-100">
                        </div>
                        <div>
                            <label for="heightInput" class="block text-xs font-semibold text-slate-600 dark:text-slate-400 mb-1">Height (px)</label>
                            <input type="number" id="heightInput" class="w-full p-2.5 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl font-mono text-slate-900 dark:text-slate-100">
                        </div>
                        <div class="flex items-end pb-2">
                            <label class="flex items-center gap-2 cursor-pointer text-xs font-semibold text-slate-700 dark:text-slate-300">
                                <input type="checkbox" id="lockAspect" checked class="rounded text-purple-600 focus:ring-purple-500">
                                <span>Lock Aspect Ratio</span>
                            </label>
                        </div>
                    </div>

                    <!-- Image Preview & Canvas Container -->
                    <div class="p-4 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-dark-border flex flex-col items-center justify-center overflow-hidden">
                        <canvas id="scalerCanvas" class="max-w-full max-h-96 rounded-lg shadow-sm"></canvas>
                        <span id="canvasDimLabel" class="text-xs font-mono text-slate-400 mt-2">Original Dimensions: 0 × 0 px</span>
                    </div>

                    <!-- Action Bar -->
                    <div class="flex flex-wrap items-center justify-between gap-4 pt-2">
                        <button type="button" id="resetImageBtn" class="px-4 py-2 text-xs font-semibold rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 transition">
                            <i class="fa-solid fa-trash-can mr-1"></i> Choose Another Image
                        </button>
                        <button type="button" id="downloadImageBtn" class="px-6 py-2.5 text-xs font-bold rounded-xl bg-purple-600 hover:bg-purple-700 text-white shadow-md shadow-purple-500/20 transition flex items-center gap-2 active:scale-95">
                            <i class="fa-solid fa-download"></i> Download Scaled Image
                        </button>
                    </div>
                </div>
            </div>
        """,
        "custom_script": """
            const dropzone = document.getElementById('dropzone');
            const fileInput = document.getElementById('imageInput');
            const controlsArea = document.getElementById('controlsArea');
            const widthInput = document.getElementById('widthInput');
            const heightInput = document.getElementById('heightInput');
            const lockAspect = document.getElementById('lockAspect');
            const canvas = document.getElementById('scalerCanvas');
            const ctx = canvas.getContext('2d');
            const dimLabel = document.getElementById('canvasDimLabel');
            const resetBtn = document.getElementById('resetImageBtn');
            const downloadBtn = document.getElementById('downloadImageBtn');
            const presetBtns = document.querySelectorAll('.preset-btn');

            let originalImage = null;
            let aspectRatio = 1;

            dropzone.addEventListener('click', () => fileInput.click());
            dropzone.addEventListener('dragover', (e) => { e.preventDefault(); dropzone.classList.add('border-purple-500'); });
            dropzone.addEventListener('dragleave', () => dropzone.classList.remove('border-purple-500'));
            dropzone.addEventListener('drop', (e) => {
                e.preventDefault();
                dropzone.classList.remove('border-purple-500');
                if (e.dataTransfer.files.length) handleFile(e.dataTransfer.files[0]);
            });

            fileInput.addEventListener('change', (e) => {
                if (e.target.files.length) handleFile(e.target.files[0]);
            });

            function handleFile(file) {
                if (!file.type.startsWith('image/')) return;
                const reader = new FileReader();
                reader.onload = (event) => {
                    const img = new Image();
                    img.onload = () => {
                        originalImage = img;
                        aspectRatio = img.width / img.height;
                        widthInput.value = img.width;
                        heightInput.value = img.height;
                        dropzone.classList.add('hidden');
                        controlsArea.classList.remove('hidden');
                        renderCanvas(img.width, img.height);
                    };
                    img.src = event.target.result;
                };
                reader.readAsDataURL(file);
            }

            function renderCanvas(w, h) {
                canvas.width = w;
                canvas.height = h;
                ctx.drawImage(originalImage, 0, 0, w, h);
                dimLabel.textContent = `Rendered Output: ${w} × ${h} px`;
            }

            widthInput.addEventListener('input', () => {
                const w = parseInt(widthInput.value) || 100;
                if (lockAspect.checked) {
                    const h = Math.round(w / aspectRatio);
                    heightInput.value = h;
                    renderCanvas(w, h);
                } else {
                    renderCanvas(w, parseInt(heightInput.value) || 100);
                }
            });

            heightInput.addEventListener('input', () => {
                const h = parseInt(heightInput.value) || 100;
                if (lockAspect.checked) {
                    const w = Math.round(h * aspectRatio);
                    widthInput.value = w;
                    renderCanvas(w, h);
                } else {
                    renderCanvas(parseInt(widthInput.value) || 100, h);
                }
            });

            presetBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    const w = parseInt(btn.dataset.w);
                    const h = parseInt(btn.dataset.h);
                    lockAspect.checked = false;
                    widthInput.value = w;
                    heightInput.value = h;
                    renderCanvas(w, h);
                });
            });

            resetBtn.addEventListener('click', () => {
                originalImage = null;
                fileInput.value = '';
                controlsArea.classList.add('hidden');
                dropzone.classList.remove('hidden');
            });

            downloadBtn.addEventListener('click', () => {
                const link = document.createElement('a');
                link.download = `creatorkit-resized-${widthInput.value}x${heightInput.value}.png`;
                link.href = canvas.toDataURL('image/png');
                link.click();
            });
        """,
        "overview": """
            <h3>Client-Side Image Resizing for Creators & Bloggers</h3>
            <p>Content creators, bloggers, and social media managers frequently need to adapt visual assets into platform-specific dimensions: 16:9 for YouTube thumbnails, 1:1 for Instagram grids, 9:16 for vertical TikTok and Reels videos, and standard landscape graphics for Twitter banners and blog headers.</p>
            <p>CreatorKit Studio's <strong>Free Online Image Resizer</strong> processes images locally in your browser using HTML5 Canvas. Your images do not need to be uploaded to a server, ensuring complete privacy for unreleased thumbnails and proprietary graphics.</p>
            <p>When preparing visual assets for your website, you can also craft search-optimized titles and snippets with our <a href="../seo-meta-generator/" class="text-indigo-600 dark:text-indigo-400 font-semibold hover:underline">SEO Meta & SERP Generator</a>.</p>
        """,
        "instructions": [
            "Upload an image file (PNG, JPG, WebP, GIF, or SVG) by clicking the upload area or dragging a file from your desktop.",
            "Select a preset dimension (YouTube 1280×720, Instagram 1080×1080, TikTok/Reels 1080×1920, Twitter 1200×675) or type custom pixel dimensions.",
            "Keep 'Lock Aspect Ratio' checked to scale proportionally without distorting image proportions.",
            "Click <strong>Download Scaled Image</strong> to save your resized image directly to your device."
        ],
        "tips": [
            "For YouTube video thumbnails, 1280×720 pixels (16:9 aspect ratio) is the standard recommended dimension.",
            "Keep the aspect ratio locked when resizing portraits or product photography to avoid unnatural stretching.",
            "Because images are processed locally in your browser, you can scale high-resolution files without uploading delays or server wait times."
        ],
        "privacy": "Images are processed locally in your browser using HTML5 Canvas. Your images do not need to be uploaded to a server, ensuring your graphics remain 100% private.",
        "faqs": [
            {
                "q": "What formats does this image resizer support?",
                "a": "The resizer supports standard web formats including PNG, JPG, WebP, GIF, and SVG."
            },
            {
                "q": "Are my photos uploaded to a server?",
                "a": "No. Images are processed entirely in your web browser using HTML5 Canvas. No image data is sent to external servers."
            },
            {
                "q": "What is the recommended size for YouTube thumbnails?",
                "a": "YouTube recommends 1280×720 pixels with a 16:9 aspect ratio and a minimum width of 640 pixels."
            }
        ]
    },
    {
        "dir": "hashtag-generator",
        "canonical": "https://www.creatorkitstudio.pro/tools/hashtag-generator/",
        "title": "Free Hashtag Generator – Instagram, TikTok & Shorts | CreatorKit Studio",
        "meta_desc": "Generate relevant hashtags categorized for Instagram, TikTok, YouTube Shorts, and LinkedIn. Clean spaces, deduplicate tags, and copy sets in 1 click.",
        "keywords": "free hashtag generator, hashtag generator online, instagram hashtag maker, tiktok viral tags, youtube shorts hashtags, linkedin hashtags",
        "h1": "Free Hashtag Generator",
        "badge": "Free Hashtag Generator",
        "summary": "Generate relevant, topic-specific hashtags categorized for Instagram, TikTok, YouTube Shorts, and LinkedIn. Discover niche tags to organize and label your content across social platforms with zero server tracking.",
        "icon": "fa-tags",
        "color": "pink",
        "custom_ui": """
            <div class="space-y-5">
                <div class="space-y-2">
                    <label for="nicheInput" class="text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                        <i class="fa-solid fa-magnifying-glass text-pink-500"></i> Enter Keyword, Niche, or Topic:
                    </label>
                    <div class="flex gap-2">
                        <input type="text" id="nicheInput" placeholder="e.g., fitness nutrition, saas marketing, street photography, digital art" class="flex-1 p-3 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-pink-500 font-sans transition">
                        <button id="generateTagsBtn" class="px-5 py-3 text-xs font-bold rounded-xl bg-pink-600 hover:bg-pink-700 text-white shadow-md shadow-pink-500/20 transition flex items-center gap-2">
                            <i class="fa-solid fa-wand-magic-sparkles"></i> Generate
                        </button>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-4 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-dark-border space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-slate-700 dark:text-slate-300"><i class="fa-brands fa-instagram text-pink-500 mr-1"></i> Instagram Niche Tags</span>
                            <button class="copy-tag-btn text-[11px] font-semibold text-pink-600 dark:text-pink-400 hover:underline" data-target="igTags">Copy Set</button>
                        </div>
                        <div id="igTags" class="text-xs font-mono text-slate-600 dark:text-slate-300 leading-relaxed min-h-[4rem] flex items-center">Enter a keyword above to generate tags...</div>
                    </div>

                    <div class="p-4 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-dark-border space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-slate-700 dark:text-slate-300"><i class="fa-brands fa-tiktok text-cyan-400 mr-1"></i> TikTok Viral Tags</span>
                            <button class="copy-tag-btn text-[11px] font-semibold text-pink-600 dark:text-pink-400 hover:underline" data-target="ttTags">Copy Set</button>
                        </div>
                        <div id="ttTags" class="text-xs font-mono text-slate-600 dark:text-slate-300 leading-relaxed min-h-[4rem] flex items-center">Enter a keyword above to generate tags...</div>
                    </div>

                    <div class="p-4 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-dark-border space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-slate-700 dark:text-slate-300"><i class="fa-brands fa-youtube text-red-500 mr-1"></i> Shorts Discovery Tags</span>
                            <button class="copy-tag-btn text-[11px] font-semibold text-pink-600 dark:text-pink-400 hover:underline" data-target="ytTags">Copy Set</button>
                        </div>
                        <div id="ytTags" class="text-xs font-mono text-slate-600 dark:text-slate-300 leading-relaxed min-h-[4rem] flex items-center">Enter a keyword above to generate tags...</div>
                    </div>

                    <div class="p-4 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-dark-border space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-slate-700 dark:text-slate-300"><i class="fa-brands fa-linkedin text-blue-500 mr-1"></i> LinkedIn Professional Tags</span>
                            <button class="copy-tag-btn text-[11px] font-semibold text-pink-600 dark:text-pink-400 hover:underline" data-target="liTags">Copy Set</button>
                        </div>
                        <div id="liTags" class="text-xs font-mono text-slate-600 dark:text-slate-300 leading-relaxed min-h-[4rem] flex items-center">Enter a keyword above to generate tags...</div>
                    </div>
                </div>

                <div class="flex justify-end">
                    <button id="copyAllTagsBtn" class="px-5 py-2.5 text-xs font-bold rounded-xl bg-slate-800 dark:bg-slate-700 hover:bg-slate-900 text-white shadow-sm transition flex items-center gap-2">
                        <i class="fa-regular fa-copy"></i> Copy Master Tag Set
                    </button>
                </div>
            </div>
        """,
        "custom_script": """
            const nicheInput = document.getElementById('nicheInput');
            const generateBtn = document.getElementById('generateTagsBtn');
            const igTagsEl = document.getElementById('igTags');
            const ttTagsEl = document.getElementById('ttTags');
            const ytTagsEl = document.getElementById('ytTags');
            const liTagsEl = document.getElementById('liTags');
            const copyAllBtn = document.getElementById('copyAllTagsBtn');

            function generate() {
                const query = nicheInput.value.trim().toLowerCase().replace(/[^a-z0-9\\s]/g, '');
                if (!query) return;
                const terms = query.split(/\\s+/).filter(Boolean);
                const primary = terms[0] || 'creator';
                const secondary = terms[1] || 'tips';

                const ig = [`#${primary}`, `#${primary}life`, `#${primary}tips`, `#${primary}creator`, `#${primary}community`, `#${primary}daily`, `#${secondary}`, `#${primary}goals`];
                const tt = [`#${primary}`, `#fyp`, `#viral${primary}`, `#${primary}hacks`, `#learnontiktok`, `#${primary}tutorial`, `#trending`];
                const yt = [`#shorts`, `#${primary}`, `#${primary}tips`, `#youtubeshorts`, `#${secondary}`, `#howTo${primary.charAt(0).toUpperCase() + primary.slice(1)}`];
                const li = [`#${primary}`, `#${primary}strategy`, `#innovation`, `#leadership`, `#digitalmarketing`, `#growth`];

                igTagsEl.textContent = ig.join(' ');
                ttTagsEl.textContent = tt.join(' ');
                ytTagsEl.textContent = yt.join(' ');
                liTagsEl.textContent = li.join(' ');
            }

            generateBtn.addEventListener('click', generate);
            nicheInput.addEventListener('keydown', (e) => { if (e.key === 'Enter') generate(); });

            document.querySelectorAll('.copy-tag-btn').forEach(btn => {
                btn.addEventListener('click', async () => {
                    const targetId = btn.dataset.target;
                    const text = document.getElementById(targetId).textContent;
                    if (text && !text.includes('Enter a keyword')) {
                        await navigator.clipboard.writeText(text);
                        const orig = btn.textContent;
                        btn.textContent = 'Copied!';
                        setTimeout(() => btn.textContent = orig, 1500);
                    }
                });
            });

            copyAllBtn.addEventListener('click', async () => {
                const all = [igTagsEl.textContent, ttTagsEl.textContent, ytTagsEl.textContent, liTagsEl.textContent]
                    .filter(t => !t.includes('Enter a keyword'))
                    .join(' ');
                if (all) {
                    await navigator.clipboard.writeText(all);
                    copyAllBtn.innerHTML = '<i class="fa-solid fa-check text-emerald-400"></i> Copied All!';
                    setTimeout(() => copyAllBtn.innerHTML = '<i class="fa-regular fa-copy"></i> Copy Master Tag Set', 1500);
                }
            });
        """,
        "overview": """
            <h3>Topic Discovery & Tag Organization for Social Content</h3>
            <p>Hashtags help categorize content and make posts discoverable to users searching for specific topics across social platforms. Using focused, topic-specific tags makes it easier for your audience to find relevant posts, tutorials, and discussions.</p>
            <p>CreatorKit Studio's <strong>Free Hashtag Generator</strong> organizes tags by platform format, allowing you to quickly generate and copy relevant keyword groupings for Instagram, TikTok, YouTube Shorts, and LinkedIn directly in your browser.</p>
            <p>If you are repurposing video transcripts into social captions, you can first clean timestamp headers using our <a href="../srt-caption-cleaner/" class="text-indigo-600 dark:text-indigo-400 font-semibold hover:underline">SRT Caption Cleaner</a>.</p>
        """,
        "instructions": [
            "Enter a topic keyword or niche phrase into the search box (e.g. 'digital marketing' or 'fitness nutrition').",
            "Click <strong>Generate</strong> to create platform-tailored hashtag sets for Instagram, TikTok, YouTube Shorts, and LinkedIn.",
            "Click 'Copy Set' next to any platform card, or click <strong>Copy Master Tag Set</strong> to copy all generated tags.",
            "Paste the tags into your social post caption or notes."
        ],
        "tips": [
            "Hashtag recommendations vary by platform, content type, and audience. Focus on relevant, specific hashtags rather than adding large numbers of unrelated tags.",
            "Mix broader topic tags with specific sub-niche tags that directly match what is shown in your post.",
            "Avoid repetitive or irrelevant tags to keep your posts clear and focused for your followers."
        ],
        "privacy": "All hashtag suggestions are generated locally in your web browser. Your search queries and keywords are not recorded or sent to any server.",
        "faqs": [
            {
                "q": "How many hashtags should I use on my posts?",
                "a": "Hashtag recommendations vary by platform and audience. It is generally best to focus on a targeted set of relevant, topic-specific hashtags rather than adding excessive tags."
            },
            {
                "q": "Should hashtags be placed in the caption or comments?",
                "a": "Both placements allow your tags to be discovered. Placing them directly in the caption ensures they are immediately active when your post goes live."
            }
        ]
    },
    {
        "dir": "teleprompter",
        "canonical": "https://www.creatorkitstudio.pro/tools/teleprompter/",
        "title": "Online Teleprompter – Free Fullscreen Script Prompter | CreatorKit Studio",
        "meta_desc": "Free online fullscreen teleprompter for creators and presenters. Smooth auto-scroll, speed controls, font resizing, and beam-splitter mirror rig mode.",
        "keywords": "online teleprompter, free teleprompter online, fullscreen script prompter, mirror teleprompter browser, video recording prompter",
        "h1": "Online Teleprompter",
        "badge": "Online Teleprompter",
        "summary": "A distraction-free online video teleprompter with smooth scrolling, adjustable scroll speed (1–10x), font resizing (24–72px), keyboard play/pause controls, and horizontal mirror mode for prompter glass rigs. Runs 100% in your browser.",
        "icon": "fa-chalkboard-user",
        "color": "indigo",
        "custom_ui": """
            <div class="space-y-5">
                <div class="space-y-2">
                    <label for="promptInput" class="text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                        <i class="fa-solid fa-file-lines text-indigo-500"></i> Video Script / Presentation Copy:
                    </label>
                    <textarea id="promptInput" rows="8" placeholder="Paste your video script, speech, or talking points here..." class="w-full p-3.5 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 font-sans resize-y custom-scrollbar transition"></textarea>
                </div>

                <div class="flex flex-wrap items-center justify-between gap-4 p-4 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-dark-border">
                    <div class="flex items-center gap-4 text-xs font-medium text-slate-600 dark:text-slate-300">
                        <span><i class="fa-solid fa-keyboard text-indigo-500 mr-1"></i> Spacebar = Play / Pause</span>
                        <span><i class="fa-solid fa-arrows-up-down text-indigo-500 mr-1"></i> Up/Down = Adjust Speed</span>
                    </div>
                    <button id="launchPrompterBtn" class="px-6 py-2.5 text-xs font-bold rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white shadow-md shadow-indigo-500/20 transition flex items-center gap-2 active:scale-95">
                        <i class="fa-solid fa-play"></i> Launch Fullscreen Prompter
                    </button>
                </div>

                <!-- Fullscreen Overlay Viewport (Hidden until activated) -->
                <div id="prompterModal" class="fixed inset-0 z-50 bg-black text-white hidden flex-col select-none">
                    <div class="flex items-center justify-between px-6 py-3 bg-slate-900/90 border-b border-slate-800 text-xs">
                        <div class="flex items-center gap-4">
                            <button id="togglePlayBtn" class="px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white font-bold transition flex items-center gap-1.5">
                                <i id="playIcon" class="fa-solid fa-play"></i> <span id="playLabel">Play (Space)</span>
                            </button>
                            <div class="flex items-center gap-2">
                                <span>Speed:</span>
                                <input type="range" id="speedSlider" min="1" max="10" value="3" class="w-24 accent-indigo-500">
                                <span id="speedValue" class="font-mono">3x</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <span>Font:</span>
                                <input type="range" id="fontSlider" min="24" max="72" value="42" class="w-24 accent-indigo-500">
                                <span id="fontValue" class="font-mono">42px</span>
                            </div>
                            <label class="flex items-center gap-1.5 cursor-pointer">
                                <input type="checkbox" id="mirrorToggle" class="rounded accent-indigo-500">
                                <span>Mirror Rig</span>
                            </label>
                        </div>
                        <button id="closePrompterBtn" class="px-3 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-700 text-white font-bold transition">
                            <i class="fa-solid fa-xmark mr-1"></i> Exit (Esc)
                        </button>
                    </div>
                    <div id="prompterScrollArea" class="flex-1 overflow-y-auto px-12 sm:px-24 md:px-48 py-24 text-center custom-scrollbar scroll-smooth">
                        <div id="prompterText" class="max-w-4xl mx-auto leading-relaxed font-semibold transition-all font-sans text-3xl"></div>
                        <div class="h-[60vh]"></div>
                    </div>
                </div>
            </div>
        """,
        "custom_script": """
            const promptInput = document.getElementById('promptInput');
            const launchBtn = document.getElementById('launchPrompterBtn');
            const modal = document.getElementById('prompterModal');
            const closeBtn = document.getElementById('closePrompterBtn');
            const playBtn = document.getElementById('togglePlayBtn');
            const playIcon = document.getElementById('playIcon');
            const playLabel = document.getElementById('playLabel');
            const speedSlider = document.getElementById('speedSlider');
            const speedVal = document.getElementById('speedValue');
            const fontSlider = document.getElementById('fontSlider');
            const fontVal = document.getElementById('fontValue');
            const mirrorToggle = document.getElementById('mirrorToggle');
            const scrollArea = document.getElementById('prompterScrollArea');
            const prompterText = document.getElementById('prompterText');

            let isPlaying = false;
            let animationFrameId = null;

            launchBtn.addEventListener('click', () => {
                const val = promptInput.value.trim() || 'Welcome to CreatorKit Studio Teleprompter! Paste your script into the input box to get started with seamless on-camera presentations.';
                prompterText.textContent = val;
                prompterText.style.fontSize = `${fontSlider.value}px`;
                modal.classList.remove('hidden');
                modal.classList.add('flex');
                scrollArea.scrollTop = 0;
            });

            closeBtn.addEventListener('click', closePrompter);
            function closePrompter() {
                pause();
                modal.classList.add('hidden');
                modal.classList.remove('flex');
            }

            function togglePlay() {
                if (isPlaying) pause(); else play();
            }

            function play() {
                isPlaying = true;
                playIcon.className = 'fa-solid fa-pause';
                playLabel.textContent = 'Play (Space)';
                scrollStep();
            }

            function pause() {
                isPlaying = false;
                playIcon.className = 'fa-solid fa-play';
                playLabel.textContent = 'Play (Space)';
                if (animationFrameId) cancelAnimationFrame(animationFrameId);
            }

            function scrollStep() {
                if (!isPlaying) return;
                const speed = parseFloat(speedSlider.value);
                scrollArea.scrollTop += (speed * 0.4);
                animationFrameId = requestAnimationFrame(scrollStep);
            }

            playBtn.addEventListener('click', togglePlay);
            speedSlider.addEventListener('input', () => speedVal.textContent = `${speedSlider.value}x`);
            fontSlider.addEventListener('input', () => {
                fontVal.textContent = `${fontSlider.value}px`;
                prompterText.style.fontSize = `${fontSlider.value}px`;
            });
            mirrorToggle.addEventListener('change', () => {
                if (mirrorToggle.checked) prompterText.style.transform = 'scaleX(-1)';
                else prompterText.style.transform = 'none';
            });

            window.addEventListener('keydown', (e) => {
                if (!modal.classList.contains('hidden')) {
                    if (e.code === 'Space') { e.preventDefault(); togglePlay(); }
                    if (e.code === 'Escape') { e.preventDefault(); closePrompter(); }
                }
            });
        """,
        "overview": """
            <h3>Smooth On-Camera Script Delivery for Video Creators</h3>
            <p>Recording video lessons, YouTube presentations, and live webinars is easier when you can read your speaking notes naturally without looking away from the camera lens. A teleprompter helps you maintain consistent eye contact and pacing.</p>
            <p>CreatorKit Studio's <strong>Online Teleprompter</strong> provides smooth browser-based auto-scrolling with adjustable speed, font size controls, keyboard shortcuts, and horizontal mirror mode for beam-splitter prompter glass setups.</p>
            <p>After recording your video, you can convert your exported subtitle files into clean article transcripts with our <a href="../srt-caption-cleaner/" class="text-indigo-600 dark:text-indigo-400 font-semibold hover:underline">SRT Caption Cleaner</a>.</p>
        """,
        "instructions": [
            "Paste your video script, speech notes, or outline into the text area.",
            "Click <strong>Launch Fullscreen Prompter</strong> to enter the distraction-free presentation screen.",
            "Adjust the font size slider (24–72px) and scroll speed slider (1–10x) to match your reading comfort.",
            "Press the <kbd class=\"px-1.5 py-0.5 bg-slate-800 text-white rounded\">Spacebar</kbd> on your keyboard to play or pause scrolling at any time."
        ],
        "tips": [
            "Place your browser window as close as possible to your webcam or camera lens to maintain natural eye contact.",
            "Enable 'Mirror Rig' mode when reflecting text onto physical beam-splitter teleprompter glass.",
            "Set the scroll speed so the current line stays near the top third of your display."
        ],
        "privacy": "All script text remains entirely inside your local browser session. No text is saved, stored, or transmitted to any external server.",
        "faqs": [
            {
                "q": "What is Mirror Rig mode?",
                "a": "Mirror Rig mode flips the text horizontally so it appears normal when reflected on a physical teleprompter glass rig."
            },
            {
                "q": "What keyboard shortcuts can I use?",
                "a": "Press Spacebar to play or pause auto-scrolling, and press Escape to close fullscreen mode."
            }
        ]
    },
    {
        "dir": "srt-caption-cleaner",
        "canonical": "https://www.creatorkitstudio.pro/tools/srt-caption-cleaner/",
        "title": "SRT Caption Cleaner – Convert Subtitles to Text | CreatorKit Studio",
        "meta_desc": "Clean .SRT and WebVTT subtitle files into readable text. Strip timecodes, sequence numbers, and formatting tags with zero server uploads.",
        "keywords": "SRT caption cleaner, convert srt to text, remove timecodes from srt, clean vtt captions online, video transcript cleaner free",
        "h1": "SRT Caption Cleaner",
        "badge": "SRT Caption Cleaner",
        "summary": "Convert raw .SRT and WebVTT subtitle files into clean, readable text. Automatically strips timestamps (00:00:00,000 --> 00:00:00,000), sequence numbers, and formatting tags directly in your browser.",
        "icon": "fa-closed-captioning",
        "color": "emerald",
        "custom_ui": """
            <div class="space-y-5">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                    <div class="space-y-2">
                        <div class="flex items-center justify-between">
                            <label for="srtInput" class="text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                                <i class="fa-solid fa-file-code text-emerald-500"></i> Raw .SRT / .VTT Subtitle Text
                            </label>
                            <button id="clearSrtBtn" class="text-xs text-rose-500 hover:underline">Clear</button>
                        </div>
                        <textarea id="srtInput" rows="10" placeholder="1&#10;00:00:01,000 --> 00:00:04,000&#10;Welcome to this video tutorial.&#10;&#10;2&#10;00:00:04,500 --> 00:00:08,000&#10;Today we will learn how to repurpose video transcripts." class="w-full p-3.5 text-xs font-mono bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 resize-y custom-scrollbar transition"></textarea>
                    </div>

                    <div class="space-y-2">
                        <div class="flex items-center justify-between">
                            <label for="srtOutput" class="text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                                <i class="fa-solid fa-align-left text-emerald-500"></i> Cleaned Transcript Output
                            </label>
                            <button id="copySrtBtn" class="px-3 py-1 text-xs font-semibold rounded-md bg-emerald-600 hover:bg-emerald-700 text-white shadow-sm transition flex items-center gap-1.5">
                                <i class="fa-regular fa-copy"></i> Copy Transcript
                            </button>
                        </div>
                        <textarea id="srtOutput" rows="10" readonly placeholder="Clean text transcript with timestamps removed will appear here automatically..." class="w-full p-3.5 text-sm bg-slate-100/80 dark:bg-slate-900/60 border border-slate-200 dark:border-dark-border rounded-xl text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none resize-y custom-scrollbar transition"></textarea>
                    </div>
                </div>
            </div>
        """,
        "custom_script": """
            const input = document.getElementById('srtInput');
            const output = document.getElementById('srtOutput');
            const clearBtn = document.getElementById('clearSrtBtn');
            const copyBtn = document.getElementById('copySrtBtn');

            function cleanSrt(raw) {
                if (!raw) return '';
                return raw
                    .replace(/^WEBVTT[^\n]*\n+/i, '')
                    .replace(/\d{1,2}:\d{2}:\d{2}[,\.]\d{3}\s*-->\s*\d{1,2}:\d{2}:\d{2}[,\.]\d{3}[^\n]*/g, '')
                    .replace(/^\s*\d+\s*$/gm, '')
                    .replace(/<\/?[^>]+(>|$)/g, '')
                    .replace(/\{[^\}]+\}/g, '')
                    .split(/\r?\n/).map(l => l.trim()).filter(Boolean).join('\n\n');
            }

            input.addEventListener('input', () => {
                output.value = cleanSrt(input.value);
            });

            clearBtn.addEventListener('click', () => {
                input.value = '';
                output.value = '';
            });

            copyBtn.addEventListener('click', async () => {
                if (!output.value) return;
                await navigator.clipboard.writeText(output.value);
                copyBtn.textContent = 'Copied!';
                setTimeout(() => copyBtn.innerHTML = '<i class="fa-regular fa-copy"></i> Copy Transcript', 1500);
            });
        """,
        "overview": """
            <h3>Converting Video Subtitles into Clean Transcripts</h3>
            <p>Video subtitle files exported from editing tools and platforms (such as YouTube, Premiere Pro, Final Cut, and CapCut) contain timestamp lines and numeric counters on every line. Reading or reusing raw subtitle text requires stripping these formatting headers.</p>
            <p>CreatorKit Studio's <strong>SRT Caption Cleaner</strong> processes subtitle text locally in your browser without uploading your file to a server. It automatically removes timecodes and line numbers, leaving you with clean, continuous text suitable for articles, notes, and documentation.</p>
            <p>Once your transcript is cleaned, you can generate search-ready titles and snippet descriptions using our <a href="../seo-meta-generator/" class="text-indigo-600 dark:text-indigo-400 font-semibold hover:underline">SEO Meta & SERP Generator</a>.</p>
        """,
        "instructions": [
            "Copy the raw `.srt` or `.vtt` text from your subtitle file or video editor.",
            "Paste the text into the left input area.",
            "The tool instantly strips timestamps, sequence counters, and styling tags, outputting clean text on the right.",
            "Click <strong>Copy Transcript</strong> to copy the cleaned text to your clipboard."
        ],
        "tips": [
            "Clean and standardize subtitle files to help keep your captions organized and consistent for blog articles and show notes.",
            "Use this tool to convert spoken video transcripts into readable outlines or newsletter drafts."
        ],
        "privacy": "Processes subtitle text locally in your browser without uploading your file to a server. Your transcript data remains completely private.",
        "faqs": [
            {
                "q": "Does this tool remove any spoken dialogue?",
                "a": "No. The cleaner only removes timestamp headers and line counters, keeping all your spoken words intact."
            },
            {
                "q": "Does it support both .SRT and .VTT files?",
                "a": "Yes. It handles both standard SubRip (.srt) and WebVTT (.vtt) timestamp formats."
            }
        ]
    },
    {
        "dir": "seo-meta-generator",
        "canonical": "https://www.creatorkitstudio.pro/tools/seo-meta-generator/",
        "title": "SEO Meta & SERP Generator – Title & Description Preview | CreatorKit Studio",
        "meta_desc": "Generate clear SEO page titles and meta descriptions with a live Google SERP preview. Test search snippet display with zero server tracking.",
        "keywords": "SEO meta generator, Google SERP preview tool, meta title builder, meta description preview, search snippet tester online",
        "h1": "SEO Meta & SERP Generator",
        "badge": "SEO Meta & SERP Generator",
        "summary": "Generate clear SEO page titles and meta descriptions from your topic summary, complete with a live Google Search desktop and mobile SERP preview simulation. 100% private in-browser generation.",
        "icon": "fa-magnifying-glass-chart",
        "color": "cyan",
        "custom_ui": """
            <div class="space-y-6">
                <!-- Text Input -->
                <div class="space-y-2">
                    <label for="metaInput" class="text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                        <i class="fa-solid fa-file-lines text-cyan-500"></i> Page Content / Topic Summary:
                    </label>
                    <textarea id="metaInput" rows="5" placeholder="Paste your article introduction, summary paragraph, or core topic here..." class="w-full p-3.5 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-cyan-500 font-sans resize-y custom-scrollbar transition"></textarea>
                </div>

                <!-- Live SERP Preview Card -->
                <div class="p-5 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-dark-border space-y-3 shadow-xs">
                    <span class="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
                        <i class="fa-brands fa-google text-cyan-500"></i> Live Google Search Result Preview:
                    </span>
                    <div class="p-4 bg-slate-50 dark:bg-slate-950 rounded-xl border border-slate-100 dark:border-slate-800 space-y-1">
                        <div class="text-[11px] text-slate-500 flex items-center gap-1">
                            <span>https://www.example.com</span> <i class="fa-solid fa-chevron-right text-[8px]"></i> <span id="serpSlug">article-slug</span>
                        </div>
                        <h4 id="serpTitle" class="text-base text-blue-600 dark:text-blue-400 font-medium hover:underline cursor-pointer">Your SEO Page Title Appears Here</h4>
                        <p id="serpDesc" class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">Your compelling meta description snippet will appear here within optimal search engine pixel boundaries.</p>
                    </div>
                </div>

                <!-- Generated HTML Code Output -->
                <div class="space-y-2">
                    <div class="flex items-center justify-between">
                        <label for="metaOutput" class="text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300">Generated HTML Meta Tags:</label>
                        <button id="copyMetaBtn" class="px-3 py-1 text-xs font-semibold rounded-md bg-cyan-600 hover:bg-cyan-700 text-white shadow-sm transition flex items-center gap-1.5">
                            <i class="fa-regular fa-copy"></i> Copy HTML Tags
                        </button>
                    </div>
                    <textarea id="metaOutput" rows="5" readonly class="w-full p-3.5 text-xs font-mono bg-slate-100/80 dark:bg-slate-900/60 border border-slate-200 dark:border-dark-border rounded-xl text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none custom-scrollbar transition"></textarea>
                </div>
            </div>
        """,
        "custom_script": """
            const input = document.getElementById('metaInput');
            const serpTitle = document.getElementById('serpTitle');
            const serpDesc = document.getElementById('serpDesc');
            const output = document.getElementById('metaOutput');
            const copyBtn = document.getElementById('copyMetaBtn');

            function process() {
                const val = input.value.trim().replace(/[\r\n]+/g, ' ');
                if (!val) {
                    serpTitle.textContent = 'Your SEO Page Title Appears Here';
                    serpDesc.textContent = 'Your compelling meta description snippet will appear here within optimal search engine pixel boundaries.';
                    output.value = '';
                    return;
                }
                const title = val.slice(0, 58).trim() + (val.length > 58 ? '...' : '');
                const desc = val.slice(0, 155).trim() + (val.length > 155 ? '...' : '');

                serpTitle.textContent = `${title} | CreatorKit Studio`;
                serpDesc.textContent = desc;

                output.value = `<!-- Primary Meta Tags -->\n<title>${title} | CreatorKit Studio</title>\n<meta name="description" content="${desc}">\n\n<!-- Open Graph / Facebook -->\n<meta property="og:title" content="${title}">\n<meta property="og:description" content="${desc}">`;
            }

            input.addEventListener('input', process);

            copyBtn.addEventListener('click', async () => {
                if (!output.value) return;
                await navigator.clipboard.writeText(output.value);
                copyBtn.textContent = 'Copied!';
                setTimeout(() => copyBtn.innerHTML = '<i class="fa-regular fa-copy"></i> Copy HTML Tags', 1500);
            });
        """,
        "overview": """
            <h3>Crafting Search Snippets with Live SERP Previews</h3>
            <p>Search engine result snippets give potential visitors their first impression of your webpage. A clear, accurate title and informative meta description help searchers understand whether your page answers their query.</p>
            <p>CreatorKit Studio's <strong>SEO Meta & SERP Generator</strong> helps you draft and preview your title tag and meta description within a simulated Google search snippet, helping you see how your text may appear on search results pages.</p>
            <p>Pair your optimized meta tags with properly sized share images using our <a href="../image-resizer/" class="text-indigo-600 dark:text-indigo-400 font-semibold hover:underline">Free Online Image Resizer</a>.</p>
        """,
        "instructions": [
            "Paste your article introduction, summary paragraph, or core topic into the input box.",
            "The tool generates a suggested Title Tag and Meta Description based on your text.",
            "Review how your snippet appears in the live Google Search result preview.",
            "Click <strong>Copy HTML Tags</strong> and paste the generated <code>&lt;title&gt;</code> and <code>&lt;meta&gt;</code> tags into your HTML <code>&lt;head&gt;</code>."
        ],
        "tips": [
            "Keep titles concise so they are more likely to display clearly in search results without truncation.",
            "Keep meta descriptions concise and informative. Google may truncate or rewrite snippets depending on the search query and available display space.",
            "Include your main topic naturally near the beginning of the title tag."
        ],
        "privacy": "All title and meta description generation occurs locally in your web browser. No text is transmitted or saved on external servers.",
        "faqs": [
            {
                "q": "What is a good guideline for title tag length?",
                "a": "Titles are commonly kept around 50 to 60 characters to help ensure they display clearly on most desktop and mobile search screens."
            },
            {
                "q": "How long should a meta description be?",
                "a": "Meta descriptions are commonly kept around 150 to 160 characters, though search engines may adjust the snippet displayed based on the user's specific query."
            }
        ]
    }
,
    {
        "dir": "seo-slug-generator",
        "canonical": "https://www.creatorkitstudio.pro/tools/seo-slug-generator/",
        "title": "Free SEO Slug Generator – Create Clean, SEO-Friendly URLs | CreatorKit Studio",
        "meta_desc": "Create clean, readable, SEO-friendly URL slugs from titles or phrases. Convert text into lowercase, hyphen-separated slugs directly in your browser.",
        "keywords": "SEO slug generator, URL slug generator, SEO friendly URL generator, slug generator, URL slug maker, clean URL generator",
        "h1": "Free SEO Slug Generator",
        "badge": "Free SEO Slug Generator",
        "summary": "Create clean, readable, SEO-friendly URL slugs from titles, headlines, or phrases. Convert text into lowercase, hyphen-separated slugs directly in your browser with zero server uploads.",
        "icon": "fa-link",
        "color": "indigo",
        "custom_ui": """
            <div class="space-y-6">
                <!-- Input Section -->
                <div class="space-y-2">
                    <label for="slugInput" class="text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                        <i class="fa-solid fa-file-signature text-indigo-500"></i> Page Title / Headline / Target Phrase:
                    </label>
                    <div class="relative">
                        <input type="text" id="slugInput" placeholder="e.g. 10 Best Free Tools for YouTube Creators!" class="w-full p-3.5 pr-16 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 font-sans transition">
                        <button type="button" id="clearSlugBtn" class="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-slate-400 hover:text-rose-500 transition px-2 py-1">Clear</button>
                    </div>
                </div>

                <!-- Output Section -->
                <div class="space-y-2">
                    <div class="flex items-center justify-between">
                        <label for="slugOutput" class="text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                            <i class="fa-solid fa-link text-indigo-500"></i> Generated Clean URL Slug:
                        </label>
                        <button type="button" id="copySlugBtn" class="px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm transition flex items-center gap-1.5 active:scale-95">
                            <i class="fa-regular fa-copy"></i> Copy Slug
                        </button>
                    </div>
                    <input type="text" id="slugOutput" readonly placeholder="10-best-free-tools-for-youtube-creators" class="w-full p-3.5 text-sm font-mono bg-slate-100/80 dark:bg-slate-900/60 border border-slate-200 dark:border-dark-border rounded-xl text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none transition">
                </div>

                <!-- Live URL Simulation Box -->
                <div class="p-4 bg-slate-50 dark:bg-slate-900/60 rounded-xl border border-slate-200 dark:border-dark-border space-y-1.5">
                    <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1">
                        <i class="fa-solid fa-globe text-indigo-500"></i> Full URL Preview:
                    </span>
                    <div class="text-xs font-mono text-slate-600 dark:text-slate-300 break-all">
                        <span>https://example.com/blog/</span><span id="urlPreviewSlug" class="text-indigo-600 dark:text-indigo-400 font-bold">10-best-free-tools-for-youtube-creators</span>/
                    </div>
                </div>
            </div>
        """,
        "custom_script": """
            const input = document.getElementById('slugInput');
            const output = document.getElementById('slugOutput');
            const preview = document.getElementById('urlPreviewSlug');
            const copyBtn = document.getElementById('copySlugBtn');
            const clearBtn = document.getElementById('clearSlugBtn');

            function generateSlug(text) {
                if (!text) return '';
                return text
                    .toString()
                    .normalize('NFD')
                    .replace(/[\u0300-\u036f]/g, '')
                    .toLowerCase()
                    .trim()
                    .replace(/[^a-z0-9\s-]/g, '')
                    .replace(/[\s_]+/g, '-')
                    .replace(/^-+|-+$/g, '');
            }

            function update() {
                const val = input.value;
                const slug = generateSlug(val);
                output.value = slug;
                preview.textContent = slug || 'your-slug-here';
            }

            input.addEventListener('input', update);

            clearBtn.addEventListener('click', () => {
                input.value = '';
                update();
                input.focus();
            });

            copyBtn.addEventListener('click', async () => {
                if (!output.value) return;
                await navigator.clipboard.writeText(output.value);
                copyBtn.innerHTML = '<i class="fa-solid fa-check text-emerald-400"></i> Copied!';
                setTimeout(() => {
                    copyBtn.innerHTML = '<i class="fa-regular fa-copy"></i> Copy Slug';
                }, 1500);
            });
        """,
        "overview": """
            <h3>What is a URL Slug?</h3>
            <p>A URL slug is the readable portion of a web address that identifies a specific page or article (for example, in <code>example.com/blog/seo-slug-generator/</code>, the slug is <code>seo-slug-generator</code>). Slugs help both readers and search engine crawlers understand what content the page contains before opening it.</p>
            <p>CreatorKit Studio's <strong>Free SEO Slug Generator</strong> automatically formats headlines, article titles, or product names into clean, lowercase, hyphen-separated slugs directly in your web browser. Accents, punctuation marks, and extraneous spaces are sanitized locally with zero server requests.</p>
            <p>When optimizing your webpage metadata, pair your clean URL slugs with descriptive headlines using our <a href="../seo-meta-generator/" class="text-indigo-600 dark:text-indigo-400 font-semibold hover:underline">SEO Meta & SERP Generator</a>.</p>
        """,
        "instructions": [
            "Type or paste your page title, blog headline, or topic phrase into the input field.",
            "The tool instantly converts the text to lowercase, replaces spaces with hyphens, and removes invalid punctuation.",
            "Review the simulated web address in the live Full URL Preview container.",
            "Click <strong>Copy Slug</strong> to transfer the formatted string directly into your CMS permalink editor or HTML router."
        ],
        "tips": [
            "Keep slugs descriptive and reasonably concise so they are easy for human readers to remember and share.",
            "Use hyphens to separate words rather than underscores or spaces for standard web address readability.",
            "Avoid keyword stuffing: write clear, readable phrases that accurately reflect the page content rather than long strings of keywords.",
            "Avoid changing established URLs on live pages whenever possible. If you must change an active URL, set up a 301 redirect from the old URL to the new one to preserve incoming links."
        ],
        "privacy": "All slug conversion occurs 100% locally inside your web browser using client-side JavaScript. No headlines, keywords, or text inputs are ever sent to or stored on an external server.",
        "faqs": [
            {
                "q": "What is an SEO slug?",
                "a": "An SEO slug is the human-readable part of a URL that identifies a specific page on a website, typically formatted in lowercase with hyphens between words."
            },
            {
                "q": "Should URL slugs always be lowercase?",
                "a": "Yes. While domain names are case-insensitive, URL paths on many web servers can be case-sensitive. Using all lowercase characters avoids broken links and duplicate content issues."
            },
            {
                "q": "Should I use hyphens or underscores in slugs?",
                "a": "Hyphens are standard for URL slugs because web crawlers and browsers treat hyphens as natural word separators, whereas underscores can concatenate words."
            },
            {
                "q": "Should a slug contain keywords?",
                "a": "Including one or two words that describe the core topic helps users understand what the page is about before clicking. Avoid adding repetitive or unnecessary keywords."
            },
            {
                "q": "How long should a URL slug be?",
                "a": "A slug is typically most effective when kept between 3 to 6 words. Shorter slugs are easier to read, copy, and share on social media."
            },
            {
                "q": "Can I change an existing URL slug?",
                "a": "You can change a slug, but changing established URLs can break existing links and bookmarks. If you must rename an existing page, always implement a permanent 301 redirect from the old URL to the new URL."
            }
        ]
    }
]

def generate_tool_html(t):
    faqs_schema = [
        {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
        for f in t["faqs"]
    ]
    schema_json = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebApplication",
                "name": t["title"],
                "url": t["canonical"],
                "description": t["meta_desc"],
                "applicationCategory": "UtilitiesApplication",
                "operatingSystem": "All",
                "browserRequirements": "Requires JavaScript. Requires HTML5.",
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD"
                }
            },
            {
                "@type": "FAQPage",
                "mainEntity": faqs_schema
            }
        ]
    }, indent=2)

    instructions_html = "".join([f"<li>{step}</li>" for step in t["instructions"]])
    tips_html = "".join([f"<li>{tip}</li>" for tip in t["tips"]])

    faqs_html = "".join([
        f"""<details class="group bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl p-4 transition [&_summary::-webkit-details-marker]:hidden" {"open" if i == 0 else ""}>
            <summary class="flex items-center justify-between cursor-pointer font-semibold text-xs md:text-sm text-slate-900 dark:text-white">
                <span>{f['q']}</span>
                <span class="ml-2 text-slate-400 group-open:rotate-180 transition-transform">
                    <i class="fa-solid fa-chevron-down text-xs"></i>
                </span>
            </summary>
            <p class="mt-3 text-xs text-slate-600 dark:text-slate-400 leading-relaxed">{f['a']}</p>
        </details>"""
        for i, f in enumerate(t["faqs"])
    ])

    other_tools = [x for x in TOOLS_PHASE1 if x["dir"] != t["dir"]]
    related_html = "".join([
        f"""<a href="../{ot['dir']}/" class="p-3.5 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-dark-border hover:border-indigo-500 transition flex items-center gap-2.5 text-xs font-semibold text-slate-800 dark:text-slate-200 group">
            <i class="fa-solid {ot['icon']} text-indigo-500 group-hover:scale-110 transition-transform"></i>
            <span>{ot['h1']}</span>
        </a>"""
        for ot in other_tools
    ])

    return f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-8J6Z3C5EZ3"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());

      gtag('config', 'G-8J6Z3C5EZ3');
    </script>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']}</title>
    <meta name="description" content="{t['meta_desc']}">
    <meta name="keywords" content="{t['keywords']}">
    <meta name="author" content="CreatorKit Studio">
    <meta name="robots" content="index, follow">
    <meta name="google-site-verification" content="WM4c52x0WOHkjYTAqQMRLdBSMGOo3aG7IoGemVJVte8" />

    <!-- Canonical URL -->
    <link rel="canonical" href="{t['canonical']}">

    <!-- Force Cache-Busting Meta Tags -->
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="0" />

    <!-- Google AdSense Verification & Publisher Script -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5863857969717583" crossorigin="anonymous"></script>

    <!-- Open Graph / Meta -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{t['title']}">
    <meta property="og:description" content="{t['meta_desc']}">
    <meta property="og:url" content="{t['canonical']}">

    <!-- Favicon & App Icons -->
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🛠️</text></svg>">
    <link rel="icon" type="image/png" sizes="32x32" href="../../favicon.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../../favicon.png">

    <!-- Schema.org JSON-LD for WebApplication & FAQPage -->
    <script type="application/ld+json">
{schema_json}
    </script>

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{ 50: '#eef2ff', 100: '#e0e7ff', 500: '#6366f1', 600: '#4f46e5', 700: '#4338ca' }},
                        dark: {{ bg: '#0b0f19', surface: '#111827', border: '#1f2937', text: '#f3f4f6' }}
                    }}
                }}
            }}
        }};
    </script>

    <!-- FontAwesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../style.css?v=2.3.0">
</head>
<body class="bg-slate-50 dark:bg-dark-bg text-slate-900 dark:text-dark-text antialiased min-h-screen flex flex-col font-['Inter',sans-serif]">

    <!-- Top Navbar -->
    <header class="bg-white dark:bg-dark-surface border-b border-slate-200 dark:border-dark-border sticky top-0 z-40 shadow-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <a href="../../index.html" class="flex items-center gap-2.5 group" title="Return to CreatorKit Studio Homepage">
                    <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 to-indigo-400 flex items-center justify-center text-white shadow-md shadow-indigo-500/20 group-hover:scale-105 transition-transform">
                        <i class="fa-solid fa-wand-magic-sparkles text-sm"></i>
                    </div>
                    <div>
                        <span class="text-base font-extrabold tracking-tight bg-gradient-to-r from-slate-900 to-slate-700 dark:from-white dark:to-slate-300 bg-clip-text text-transparent">CreatorKit</span>
                        <span class="text-[10px] font-bold uppercase tracking-wider text-indigo-500 block leading-none">Studio</span>
                    </div>
                </a>
            </div>

            <!-- Header Navigation -->
            <nav class="hidden md:flex items-center gap-4 text-xs font-semibold">
                <a href="../" class="px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1.5">
                    <i class="fa-solid fa-layer-group text-indigo-500"></i> Tools Directory
                </a>
                <a href="../../index.html#blogger" class="px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1.5">
                    <i class="fa-solid fa-feather text-amber-500"></i> Blogger Mode
                </a>
                <a href="../../index.html#creator" class="px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1.5">
                    <i class="fa-solid fa-video text-pink-500"></i> Creator Mode
                </a>
            </nav>

            <!-- Theme Toggle & Main App Button -->
            <div class="flex items-center gap-2">
                <button id="themeToggleBtn" aria-label="Toggle Theme" class="p-2 text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-lg transition">
                    <i id="themeIcon" class="fa-solid fa-moon text-base"></i>
                </button>
                <a href="../../index.html" class="px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm transition flex items-center gap-1.5">
                    <i class="fa-solid fa-table-cells"></i> <span class="hidden sm:inline">Suite Dashboard</span>
                </a>
            </div>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="max-w-5xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8 space-y-8 flex-1">
        
        <!-- Breadcrumb Navigation -->
        <nav class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
            <a href="../../index.html" class="hover:text-indigo-500 transition">CreatorKit Studio</a>
            <i class="fa-solid fa-chevron-right text-[10px]"></i>
            <a href="../" class="hover:text-indigo-500 transition">Tools Directory</a>
            <i class="fa-solid fa-chevron-right text-[10px]"></i>
            <span class="text-slate-800 dark:text-slate-200 font-semibold">{t['h1']}</span>
        </nav>

        <!-- Header Banner Ad Placeholder -->
        <div class="w-full">
            <div class="adsense-slot adsense-placeholder w-full rounded-xl border-2 border-dashed border-slate-300 dark:border-slate-700 flex flex-col items-center justify-center text-slate-400 dark:text-slate-500 text-xs gap-1 p-3 bg-white/40 dark:bg-slate-800/30 overflow-hidden text-center shadow-sm" style="min-height: 90px; height: 90px;">
                <span class="font-mono uppercase tracking-widest text-[10px] bg-slate-200 dark:bg-slate-700 px-2 py-0.5 rounded text-slate-600 dark:text-slate-300">Advertisement</span>
                <span class="flex items-center gap-1 font-mono text-[11px]"><i class="fa-brands fa-google text-indigo-500"></i> Google AdSense Leaderboard (Responsive)</span>
            </div>
        </div>

        <!-- Tool Header -->
        <div class="space-y-2">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 border border-indigo-200/60 dark:border-indigo-800/40">
                <i class="fa-solid {t['icon']}"></i> {t['badge']}
            </div>
            <h1 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-slate-900 dark:text-white leading-tight">{t['h1']}</h1>
            <p class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed max-w-3xl">{t['summary']}</p>
        </div>

        <!-- Interactive Tool Card -->
        <div class="bg-white dark:bg-dark-surface rounded-2xl border border-slate-200 dark:border-dark-border p-5 sm:p-6 shadow-sm">
            {t['custom_ui']}
        </div>

        <!-- Structured Usage Instructions Card -->
        <section class="bg-slate-50 dark:bg-slate-900/60 p-6 rounded-2xl border border-slate-200 dark:border-dark-border space-y-4">
            <h2 class="text-lg font-bold text-slate-900 dark:text-white flex items-center gap-2">
                <i class="fa-solid fa-circle-info text-indigo-500"></i> How to Use This Tool
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="space-y-2">
                    <h3 class="text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400">Step-by-Step Instructions:</h3>
                    <ol class="list-decimal pl-5 text-xs text-slate-600 dark:text-slate-300 space-y-1.5 leading-relaxed">
                        {instructions_html}
                    </ol>
                </div>
                <div class="space-y-2">
                    <h3 class="text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400">Practical Tips & Guidelines:</h3>
                    <ul class="list-disc pl-5 text-xs text-slate-600 dark:text-slate-300 space-y-1.5 leading-relaxed">
                        {tips_html}
                    </ul>
                </div>
            </div>
        </section>

        <!-- In-Content Ad Placeholder -->
        <div class="w-full">
            <div class="adsense-slot adsense-placeholder w-full rounded-xl border-2 border-dashed border-slate-300 dark:border-slate-700 flex flex-col items-center justify-center text-slate-400 dark:text-slate-500 text-xs gap-1 p-3 bg-white/40 dark:bg-slate-800/30 overflow-hidden text-center shadow-sm" style="min-height: 90px; height: 90px;">
                <span class="font-mono uppercase tracking-widest text-[10px] bg-slate-200 dark:bg-slate-700 px-2 py-0.5 rounded text-slate-600 dark:text-slate-300">Advertisement</span>
                <span class="flex items-center gap-1 font-mono text-[11px]"><i class="fa-brands fa-google text-indigo-500"></i> Google AdSense Responsive In-Content Banner</span>
            </div>
        </div>

        <!-- Deep Educational Guide Article (400+ words) -->
        <article class="prose prose-slate dark:prose-invert max-w-none bg-white dark:bg-dark-surface p-6 sm:p-8 rounded-2xl border border-slate-200 dark:border-dark-border shadow-sm space-y-4 text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
            <h2 class="text-xl font-bold text-slate-900 dark:text-white">Overview & User Guide: {t['h1']}</h2>
            {t['overview']}
            
            <div class="mt-6 p-4 rounded-xl bg-indigo-50/50 dark:bg-indigo-950/30 border border-indigo-100 dark:border-indigo-900/40">
                <h4 class="text-xs font-bold uppercase tracking-wider text-indigo-600 dark:text-indigo-400 mb-1">
                    <i class="fa-solid fa-shield-halved"></i> 100% Client-Side Privacy Guarantee
                </h4>
                <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">{t['privacy']}</p>
            </div>
        </article>

        <!-- FAQ Accordion Section -->
        <section class="bg-white dark:bg-dark-surface p-6 sm:p-8 rounded-2xl border border-slate-200 dark:border-dark-border shadow-sm space-y-4">
            <h2 class="text-lg font-bold text-slate-900 dark:text-white flex items-center gap-2">
                <i class="fa-solid fa-circle-question text-indigo-500"></i> Frequently Asked Questions
            </h2>
            <div class="space-y-3">
                {faqs_html}
            </div>
        </section>

        <!-- Related Tools Section (Descriptive Anchor Links) -->
        <section class="space-y-3">
            <h2 class="text-sm font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">
                Explore More Free Standalone Creator Utilities:
            </h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
                {related_html}
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-white dark:bg-dark-surface border-t border-slate-200 dark:border-dark-border py-8 px-4 sm:px-6 lg:px-8 text-xs text-slate-500 dark:text-slate-400">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
            <div>
                <span class="font-bold text-slate-800 dark:text-slate-200">CreatorKit Studio</span> &copy; 2026. 100% Free Client-Side Creator Suite.
            </div>
            <div class="flex items-center gap-5 font-medium">
                <a href="../../index.html#all" class="hover:text-indigo-500">All Tools</a>
                <a href="../" class="hover:text-indigo-500">Tools Directory</a>
                <a href="../../index.html#blogger" class="hover:text-indigo-500">Blogger Suite</a>
                <a href="../../index.html#creator" class="hover:text-indigo-500">Creator Suite</a>
            </div>
        </div>
    </footer>

    <!-- Theme & Tool Logic Script -->
    <script>
        // Theme Toggle
        const themeBtn = document.getElementById('themeToggleBtn');
        const themeIcon = document.getElementById('themeIcon');
        themeBtn.addEventListener('click', () => {{
            const isDark = document.documentElement.classList.toggle('dark');
            localStorage.setItem('creatorkit_theme', isDark ? 'dark' : 'light');
            themeIcon.className = isDark ? 'fa-solid fa-sun text-base text-amber-400' : 'fa-solid fa-moon text-base text-slate-600';
        }});
        if (localStorage.getItem('creatorkit_theme') === 'light') {{
            document.documentElement.classList.remove('dark');
            themeIcon.className = 'fa-solid fa-moon text-base text-slate-600';
        }} else {{
            document.documentElement.classList.add('dark');
            themeIcon.className = 'fa-solid fa-sun text-base text-amber-400';
        }}

        // Tool-Specific Interactive Engine
        {t['custom_script']}
    </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tools_dir = os.path.join(base_dir, "tools")
    os.makedirs(tools_dir, exist_ok=True)

    for t in TOOLS_PHASE1:
        tool_folder = os.path.join(tools_dir, t["dir"])
        os.makedirs(tool_folder, exist_ok=True)
        html_path = os.path.join(tool_folder, "index.html")
        content = generate_tool_html(t)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {t['dir']}/index.html ({len(content)} bytes)")

if __name__ == "__main__":
    main()
