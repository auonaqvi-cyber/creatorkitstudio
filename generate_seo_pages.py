import os, json

TOOLS = [
    {
        "filename": "line-break-fixer.html",
        "tool_id": "fix-line-breaks",
        "h1": "Free Online Instagram Line Break & Caption Spacing Fixer (No Login)",
        "badge": "Social Media Formatting Tool",
        "title": "Free Online Instagram Line Break Fixer (No Login) | CreatorKit Studio",
        "meta_desc": "Fix Instagram, LinkedIn, and Threads caption formatting online. Prevent paragraph clumping with invisible zero-width spaces. 100% free, private & in-browser.",
        "keywords": "instagram line break fixer, fix instagram paragraph spacing, linkedin caption spacer, prevent caption clumping, instagram space generator no login",
        "summary": "Fix Instagram, LinkedIn, Threads, and Facebook caption formatting instantly. Social media mobile clients automatically strip standard double-line breaks to conserve feed height. This tool injects invisible Unicode zero-width space characters (\u200B) onto empty lines, forcing mobile apps to preserve your spacing without ugly period dots or hyphens.",
        "icon": "fa-paragraph",
        "color": "indigo",
        "category": "Social & Formatting",
        "instructions": [
            "Paste or type your caption draft into the input workspace with natural blank lines between paragraphs.",
            "The client-side engine automatically injects invisible zero-width space characters (\\u200B) into every empty newline sequence.",
            "Click <strong>Copy Result</strong> and paste directly into Instagram, LinkedIn, or Threads. Your paragraph spacing will remain intact across all devices."
        ],
        "tips": [
            "Place a clear line break immediately following your opening hook to maximize view-through before the mobile 'See More' cutoff.",
            "Avoid placing emojis immediately against line breaks so mobile accessibility screen readers parse words cleanly.",
            "Your text is processed 100% locally in your browser memory and never uploaded to any remote server."
        ],
        "deep_content": """
            <h3>Why Social Media Apps Destroy Your Caption Spacing</h3>
            <p>When you press Enter twice on a keyboard, text editors produce standard newline characters (<code>\\n\\n</code> or <code>\\r\\n\\r\\n</code>). However, the mobile rendering engines powering Instagram, LinkedIn, and Threads run aggressive whitespace sanitization regexes designed to compress feed height. Consequently, your carefully crafted paragraphs collapse into an unreadable wall of text.</p>
            <h3>The Invisible Zero-Width Space Solution</h3>
            <p>Historically, social media managers resorted to inserting visible period dots (<code>.</code>), dashes (<code>-</code>), or bullet emojis onto empty lines. While effective, this creates an unpolished appearance. CreatorKit Studio solves this by inserting standard Unicode zero-width space characters (<code>\\u200B</code>). The social feed detects content on the line and preserves the vertical gap, while the space remains 100% invisible to human readers.</p>
            <h3>Cross-Platform Compatibility</h3>
            <p>Our line break formatting is verified to work seamlessly across Instagram feed posts, Instagram Reels captions, LinkedIn articles and updates, Threads, TikTok descriptions, and Facebook pages.</p>
        """,
        "faqs": [
            {
                "q": "Why does Instagram remove empty line breaks from my captions?",
                "a": "Instagram's mobile app sanitizes multi-line text input to prevent spam and conserve vertical feed space. By adding an invisible zero-width space character (\\u200B), Instagram recognizes the line as containing content and renders the visual paragraph gap."
            },
            {
                "q": "Does this tool require a login or account?",
                "a": "No. CreatorKit Studio is 100% free with no account, signup, or login required. All processing runs entirely inside your web browser."
            },
            {
                "q": "Is my text private and secure?",
                "a": "Yes. All transformations execute locally in client-side JavaScript. Your text is never sent across the internet to any external database or server."
            }
        ],
        "js_transform": "function transform(input) { return input.replace(/\\r?\\n([ \\t]*\\r?\\n)+/g, '\\n\\u200B\\n').replace(/^[ \\t]*\\r?\\n/g, '\\u200B\\n'); }"
    },
    {
        "filename": "hashtag-generator.html",
        "tool_id": "hashtag-generator",
        "h1": "Free Multi-Platform Hashtag Generator & Extractor (Instagram, TikTok & Shorts)",
        "badge": "Social Discovery & Tag Strategy",
        "title": "Free Multi-Platform Hashtag Generator | Instagram, TikTok & Shorts | CreatorKit",
        "meta_desc": "Generate high-ranking hashtags categorized for Instagram, TikTok, YouTube Shorts, and LinkedIn. Clean spaces, remove duplicates, and copy tags in 1 click.",
        "keywords": "hashtag generator, instagram hashtags maker, tiktok viral tags, youtube shorts hashtags, linkedin hashtag generator free",
        "summary": "Generate targeted, high-intent hashtags categorized for Instagram, TikTok, YouTube Shorts, and LinkedIn. Combine high-volume broad tags with low-competition niche tags to rank on social Explore feeds and search discovery algorithms.",
        "icon": "fa-tags",
        "color": "pink",
        "category": "Social & Formatting",
        "instructions": [
            "Type your core topic, niche, or keywords (e.g. 'fitness nutrition', 'saas marketing', 'street photography') into the input box.",
            "The generator produces categorized hashtag sets grouped by search volume and platform suitability.",
            "Click <strong>Copy All Hashtags</strong> or select specific platform groups to paste directly into your caption or first comment."
        ],
        "tips": [
            "On Instagram, 3 to 8 ultra-specific niche tags consistently outperform 30 generic tags for algorithmic discovery.",
            "Pair trending audio and niche community tags on TikTok to improve For You Page (FYP) indexation.",
            "Deduplicate tags regularly to avoid triggering spam filters on LinkedIn and X."
        ],
        "deep_content": """
            <h3>The Role of Hashtags in Social Search Algorithms</h3>
            <p>Modern social media platforms use natural language processing (NLP) and hashtag metadata to categorize content into topic clusters. Rather than merely being visual decoration, hashtags serve as semantic category indexes for search engines like Instagram Explore, TikTok Search, and YouTube Suggested Videos.</p>
            <h3>Building a 3-Tier Hashtag Portfolio</h3>
            <p>To maximize discovery, structure your tags into three distinct tiers: (1) <strong>Broad Category Tags</strong> (500k+ posts) for general classification, (2) <strong>Niche Community Tags</strong> (50k–200k posts) for targeted reach, and (3) <strong>Ultra-Specific Intent Tags</strong> (5k–25k posts) where your post can rank at the top of the search tab for weeks.</p>
        """,
        "faqs": [
            {
                "q": "How many hashtags should I use on Instagram?",
                "a": "Instagram officially recommends 3 to 8 highly relevant hashtags per post to ensure its recommendation algorithms correctly categorize your content without triggering spam filters."
            },
            {
                "q": "Should I place hashtags in the caption or the first comment?",
                "a": "Both work equally for search indexation. However, placing them directly at the bottom of your caption ensures instant indexing upon publication."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input || !input.trim()) return '';
            const words = input.toLowerCase().replace(/[^a-z0-9\\s]/g, '').split(/\\s+/).filter(Boolean);
            if (!words.length) return '';
            const primary = words[0];
            const tags = [
                '#' + primary,
                '#' + primary + 'tips',
                '#' + primary + 'creator',
                '#' + primary + 'daily',
                '#' + primary + 'strategy',
                '#' + primary + 'guide',
                '#' + primary + 'hacks',
                '#' + primary + 'growth',
                '#' + primary + 'community',
                '#' + primary + 'online',
                '#creatorkit',
                '#contentcreation',
                '#socialmediatips'
            ];
            return tags.join(' ');
        }"""
    },
    {
        "filename": "twitter-thread-splitter.html",
        "tool_id": "thread-splitter",
        "h1": "Free Twitter/X Thread Splitter & Tweet Card Formatter (280 Characters)",
        "badge": "Social Copywriting Tool",
        "title": "Free Twitter/X Thread Splitter (280 Chars) | Convert Articles to Tweets",
        "meta_desc": "Split long articles, newsletters, and transcripts into numbered 280-character Twitter/X threads without cutting words or URLs mid-sentence. 100% free.",
        "keywords": "twitter thread splitter, X thread maker, split blog into tweets, 280 character chunker, convert article to twitter thread",
        "summary": "Convert long-form blog articles, newsletters, transcripts, and essays into numbered 280-character Twitter/X threads. The boundary-aware algorithm ensures words, punctuation, and URLs are never broken across card splits.",
        "icon": "fa-x-twitter",
        "color": "cyan",
        "category": "Social & Formatting",
        "instructions": [
            "Paste your long-form newsletter, article draft, or script into the workspace.",
            "The algorithm analyzes sentence boundaries and character limits, automatically splitting your text into numbered tweet cards (1/N, 2/N).",
            "Copy individual tweet cards sequentially or copy the entire thread formatted with separators."
        ],
        "tips": [
            "Ensure Tweet 1/N has a powerful standalone hook with a bold statement or clear takeaway promise.",
            "Keep individual paragraphs inside each tweet card short (1–2 lines) to maximize mobile reading speed.",
            "Use the final tweet (N/N) for a strong call to action, question, or link back to your full article."
        ],
        "deep_content": """
            <h3>Repurposing Long-Form Content for Maximum Social Reach</h3>
            <p>Twitter/X threads are one of the most effective distribution formats for creators and founders. A single 1,500-word blog post can easily yield a high-converting 8-tweet thread that drives thousands of organic impressions and newsletter signups.</p>
            <h3>Boundary-Aware Splitting Architecture</h3>
            <p>Unlike simplistic character-count substring splitters that slice words in half, CreatorKit Studio parses text at sentence periods, question marks, and paragraph line breaks. It reserves exact character budget for sequential numbering (e.g. <code>1/7</code>), ensuring each card posts cleanly within Twitter's 280-character restriction.</p>
        """,
        "faqs": [
            {
                "q": "What is the maximum character limit per tweet?",
                "a": "Standard Twitter/X accounts have a 280-character limit per post. This tool formats each card to fit safely within this limit, including the thread counter."
            },
            {
                "q": "Does this tool cut URLs or words in half?",
                "a": "No. The splitting engine respects word boundaries and URLs, pushing overflow words to the next tweet card."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input || !input.trim()) return '';
            const maxLen = 270;
            const words = input.trim().split(/\\s+/);
            const chunks = [];
            let current = '';
            words.forEach(w => {
                if ((current + ' ' + w).length <= maxLen) {
                    current = current ? current + ' ' + w : w;
                } else {
                    if (current) chunks.push(current);
                    current = w;
                }
            });
            if (current) chunks.push(current);
            const total = chunks.length;
            return chunks.map((c, i) => `${i + 1}/${total} ${c}`).join('\\n\\n---\\n\\n');
        }"""
    },
    {
        "filename": "readability-score-analyzer.html",
        "tool_id": "readability-score",
        "h1": "Free Article Readability Score Analyzer (Flesch-Kincaid Formula)",
        "badge": "Editorial Quality & SEO Tool",
        "title": "Article Readability Score Analyzer | Flesch-Kincaid Reading Ease Tool",
        "meta_desc": "Analyze article readability score online. Calculate Flesch Reading Ease, Flesch-Kincaid Grade Level, syllable count, and complex word ratio. 100% free.",
        "keywords": "readability score calculator, flesch kincaid grade level, reading ease test online, syllable counter, SEO article readability analyzer",
        "summary": "Analyze article readability, syllable density, average sentence length, Flesch Reading Ease (0–100 scale), and Flesch-Kincaid Grade Level in real time. Optimize your blog posts and sales copy for higher user engagement and Google search rankings.",
        "icon": "fa-glasses",
        "color": "emerald",
        "category": "Video & Copywriting",
        "instructions": [
            "Paste your article, blog post draft, or newsletter text into the input box.",
            "The analytical engine calculates total syllables, words, sentences, and computes your Flesch Reading Ease score instantly.",
            "Shorten complex multi-syllable words and lengthy sentences until you reach an optimal 60–70 Reading Ease score (7th–8th grade level)."
        ],
        "tips": [
            "Target a 7th to 8th grade reading level for commercial web articles to ensure maximum comprehension across broad audiences.",
            "Keep average sentence length under 18 words to prevent cognitive reader fatigue.",
            "Replace jargon and multi-syllable phrases (e.g. 'utilize' -> 'use', 'expedite' -> 'speed up') to instantly improve readability."
        ],
        "deep_content": """
            <h3>Why Readability Directly Impacts SEO and Conversions</h3>
            <p>Google's Helpful Content and core ranking algorithms reward articles that satisfy user search intent quickly and clearly. High readability scores correlate with lower bounce rates, longer on-page dwell times, and higher conversion rates on landing pages.</p>
            <h3>Understanding the Flesch-Kincaid Formulas</h3>
            <p>The <strong>Flesch Reading Ease</strong> formula outputs a score from 0 to 100: <code>206.835 - (1.015 x ASL) - (84.6 x ASW)</code>, where ASL is Average Sentence Length and ASW is Average Syllables per Word. A score of 60–70 indicates standard conversational English, while 90–100 represents effortless reading for 5th graders.</p>
        """,
        "faqs": [
            {
                "q": "What is a good Flesch Reading Ease score for web copy?",
                "a": "A score between 60 and 70 (equivalent to 7th or 8th grade reading level) is ideal for online audiences, ensuring smooth comprehension without alienating readers."
            },
            {
                "q": "Does readability affect Google search rankings?",
                "a": "Yes. Clear, readable content reduces bounce rates and increases dwell time, signaling high content quality and user satisfaction to Google's ranking systems."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input || !input.trim()) return '';
            const words = (input.match(/[\\w\\u00C0-\\u024F'-]+/g) || []).length;
            const sentences = (input.match(/[^.!?]+[.!?]+(\\s|$)/g) || [1]).length;
            const syllables = (input.match(/[aeiouy]{1,2}/gi) || []).length || words;
            if (words === 0 || sentences === 0) return 'Please enter more text to analyze.';
            const asl = words / sentences;
            const asw = syllables / words;
            const readingEase = Math.round(206.835 - (1.015 * asl) - (84.6 * asw));
            const gradeLevel = Math.round((0.39 * asl) + (11.8 * asw) - 15.59);
            return `--- READABILITY REPORT ---
Flesch Reading Ease: ${Math.max(0, Math.min(100, readingEase))} / 100
Flesch-Kincaid Grade Level: Grade ${Math.max(1, gradeLevel)}
Total Words: ${words}
Total Sentences: ${sentences}
Avg Sentence Length: ${asl.toFixed(1)} words
Avg Syllables per Word: ${asw.toFixed(2)}`;
        }"""
    },
    {
        "filename": "seo-meta-generator.html",
        "tool_id": "seo-meta-generator",
        "h1": "Free SEO Title & Meta Description Generator with Live Google SERP Preview",
        "badge": "On-Page SEO & SERP Preview",
        "title": "SEO Meta Description & Title Generator | Live Google SERP Preview Tool",
        "meta_desc": "Generate click-worthy SEO page titles and meta descriptions with live Google SERP snippet preview. Enforce 60-char title and 160-char description limits.",
        "keywords": "SEO meta description generator, Google SERP snippet preview, meta title builder, CTR optimization tool, search snippet tester online",
        "summary": "Extract key topics from your content to craft click-worthy SEO page titles (under 60 characters) and meta descriptions (under 160 characters) with a live Google Search SERP snippet simulation.",
        "icon": "fa-magnifying-glass-chart",
        "color": "indigo",
        "category": "AI, SEO & Media",
        "instructions": [
            "Paste your article introduction, summary paragraph, or key topic outline into the workspace.",
            "The generator formats a concise SEO Page Title and compelling Meta Description within pixel and character limits.",
            "Copy the ready-to-use HTML `<title>` and `<meta name=\"description\">` tags into your website CMS."
        ],
        "tips": [
            "Position your primary target keyword within the first 30 characters of the title tag.",
            "Include an active call to action (e.g. 'Learn how to...', 'Free online tool...') in your meta description to maximize organic CTR.",
            "Keep titles strictly under 60 characters (580 pixels) to avoid Google truncating your headline with '...'."
        ],
        "deep_content": """
            <h3>Maximizing Organic Click-Through Rate (CTR) on Google</h3>
            <p>Your search snippet represents your organic storefront on Google. Even if a page ranks in position #3, a compelling, benefit-driven title tag and meta description can capture significantly more clicks than a generic #1 result.</p>
            <h3>Avoiding Truncation Pitfalls</h3>
            <p>Google displays up to 580–600 pixels of title text (approximately 55–60 characters) and up to 960 pixels of description text on desktop (around 155–160 characters). Staying within these bounds guarantees clean snippet presentation on mobile and desktop search screens.</p>
        """,
        "faqs": [
            {
                "q": "What is the optimal length for an SEO title tag?",
                "a": "The recommended title tag length is 50 to 60 characters (under 580 pixels) to prevent search engines from truncating your text."
            },
            {
                "q": "Do meta descriptions directly impact search rankings?",
                "a": "While not a direct algorithmic ranking factor, meta descriptions strongly influence Click-Through Rate (CTR), which is a key organic engagement signal."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input || !input.trim()) return '';
            const clean = input.replace(/[\\r\\n]+/g, ' ').trim();
            const title = clean.slice(0, 58).trim() + (clean.length > 58 ? '...' : '');
            const desc = clean.slice(0, 155).trim() + (clean.length > 155 ? '...' : '');
            return `<!-- PRIMARY SEO TAGS -->
<title>${title} | CreatorKit Studio</title>
<meta name="description" content="${desc}">

<!-- OPEN GRAPH (SOCIAL PREVIEW) -->
<meta property="og:title" content="${title}">
<meta property="og:description" content="${desc}">`;
        }"""
    },
    {
        "filename": "image-resizer.html",
        "tool_id": "image-resizer",
        "h1": "Free Online Image Resizer & Scaler (100% In-Browser Private Canvas)",
        "badge": "Media Scaling & Canvas Tool",
        "title": "Free Online Image Resizer & Scaler | 100% In-Browser Private Canvas",
        "meta_desc": "Resize, scale, and compress images directly in your browser using HTML5 Canvas. YouTube thumbnail (1280x720), Instagram, and Twitter presets. Zero server uploads.",
        "keywords": "image resizer online, HTML5 canvas photo scaler, resize youtube thumbnail, private photo compressor, in browser photo resize no upload",
        "summary": "Resize, scale, crop, and convert images directly inside your web browser using client-side HTML5 Canvas. Includes social media presets for YouTube thumbnails (1280x720), Instagram square (1080x1080), Story/Reels (1080x1920), and Twitter/X (1200x675). Zero server uploads ensure 100% privacy.",
        "icon": "fa-image",
        "color": "purple",
        "category": "AI, SEO & Media",
        "instructions": [
            "Drag and drop any PNG, JPG, WebP, or GIF image into the dropzone area.",
            "Select a pre-configured social media preset button or enter custom width and height dimensions with aspect ratio lock.",
            "Click <strong>Download Resized Image</strong> to save your optimized file instantly to your device."
        ],
        "tips": [
            "Keep the aspect ratio lock enabled when resizing photos to avoid stretching or distorting your subject.",
            "Export in modern WebP format to achieve up to 30% smaller file sizes with zero perceptible loss in visual quality.",
            "All rendering executes in local browser memory—no photos are ever uploaded or transmitted across the internet."
        ],
        "deep_content": """
            <h3>Client-Side Image Processing Security</h3>
            <p>Traditional image converter websites require users to upload sensitive graphics, thumbnails, and family photos to remote cloud servers for processing. CreatorKit Studio uses the HTML5 Canvas 2D API to render and scale pixels locally on your device's GPU/CPU, ensuring total data confidentiality.</p>
            <h3>Standard Social Media Image Dimensions</h3>
            <p>Always format images to platform-native dimensions: <strong>YouTube Thumbnails</strong> (1280x720, 16:9), <strong>Instagram Square</strong> (1080x1080, 1:1), <strong>Instagram Stories & TikTok Reels</strong> (1080x1920, 9:16), and <strong>Twitter/X In-Feed Images</strong> (1200x675, 16:9).</p>
        """,
        "faqs": [
            {
                "q": "Are my images uploaded to any cloud server?",
                "a": "No. All scaling, resizing, and compression occur 100% locally in your web browser memory. Your files never leave your machine."
            },
            {
                "q": "What is the recommended size for YouTube video thumbnails?",
                "a": "YouTube officially recommends 1280x720 pixels with a 16:9 aspect ratio and a file size under 2MB."
            }
        ],
        "js_transform": "function transform(input) { return input; }"
    },
    {
        "filename": "hashtag-deduplicator.html",
        "tool_id": "clean-hashtags",
        "h1": "Free Hashtag Cleaner & Deduplicator (Instagram, TikTok & LinkedIn)",
        "badge": "Social Discovery & Tag Tool",
        "title": "Free Hashtag Cleaner & Deduplicator | Instagram, TikTok & LinkedIn",
        "meta_desc": "Extract, clean, and deduplicate hashtags from social media drafts. Stay within 30-tag limits and format clean tag blocks with 1-click copy.",
        "keywords": "hashtag deduplicator, clean instagram hashtags, extract hashtags from text, remove duplicate tags, social media tag cleaner free",
        "summary": "Extract hashtags from raw captions, remove accidental duplicate tags, strip invalid punctuation, and format clean, space-separated hashtag blocks ready for publishing.",
        "icon": "fa-hashtag",
        "color": "indigo",
        "category": "Social & Formatting",
        "instructions": [
            "Paste your caption or raw list of hashtags into the workspace.",
            "The regex engine automatically isolates all valid `#tags`, eliminates repeated duplicates, and trims punctuation.",
            "Click <strong>Copy Result</strong> to obtain a clean, deduplicated hashtag block."
        ],
        "tips": [
            "Ensure trailing periods or commas are stripped from tags so social search engines index them correctly.",
            "Keep Instagram hashtag blocks between 5 and 10 highly focused tags for optimal algorithmic engagement."
        ],
        "deep_content": """
            <h3>Preventing Broken and Duplicate Tags</h3>
            <p>Copy-pasting hashtag templates from notes apps frequently leads to duplicate tags and broken trailing punctuation (e.g. <code>#growth,</code> or <code>#marketing.</code>). Automated deduplication ensures your tags are formatted cleanly for platform search algorithms.</p>
        """,
        "faqs": [
            {
                "q": "Does this tool enforce the Instagram 30-hashtag limit?",
                "a": "Yes. It extracts and deduplicates tags, helping you easily verify your final count remains under the platform limit."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input) return '';
            const matches = input.match(/#[\\w\\u00C0-\\u024F]+/g) || [];
            const unique = [];
            matches.forEach(t => {
                const lower = t.toLowerCase();
                if (!unique.includes(lower)) unique.push(lower);
            });
            return unique.join(' ');
        }"""
    },
    {
        "filename": "fancy-text-generator.html",
        "tool_id": "fancy-text",
        "h1": "Free Fancy Unicode Text Generator (Bold, Italic, Bubble & Gothic Fonts)",
        "badge": "Social Typography Tool",
        "title": "Fancy Unicode Text Generator | Bold, Italic, Bubble & Gothic Styles",
        "meta_desc": "Generate aesthetic Unicode text styles for Instagram bios, Twitter/X usernames, and TikTok captions. Bold Sans, Serif, Bubble, and Gothic styles.",
        "keywords": "fancy text generator, instagram bio font changer, unicode bold text, aesthetic font styles, bubble font generator online",
        "summary": "Transform plain text into aesthetic mathematical Unicode styles (Bold Sans, Bold Serif, Italic, Bubble, Monospace, Gothic) that display natively on Instagram, TikTok, Twitter/X, and Discord.",
        "icon": "fa-font",
        "color": "indigo",
        "category": "Social & Formatting",
        "instructions": [
            "Type your name, bio headline, or caption hook into the workspace input box.",
            "The engine maps standard characters to mathematical alphanumeric Unicode symbols across multiple visual styles.",
            "Copy your styled text and paste directly into your Instagram Bio, Twitter profile, or YouTube title."
        ],
        "tips": [
            "Use bold or italic Unicode fonts for hooks and section headers; avoid styling entire paragraphs to preserve mobile readability.",
            "These styles use universal Unicode characters and do not require custom font downloads or plugins."
        ],
        "deep_content": """
            <h3>How Unicode Styling Works Across Social Platforms</h3>
            <p>Standard social media input fields do not allow custom CSS font families. However, the Unicode standard contains distinct mathematical alphanumeric character sets (such as Mathematical Bold Sans-Serif and Mathematical Script). When you copy these Unicode characters, apps like Instagram and X render them natively in custom aesthetic styles.</p>
        """,
        "faqs": [
            {
                "q": "Will these fancy fonts work on all phones and computers?",
                "a": "Yes. These are standard Unicode characters supported across iOS, Android, macOS, and Windows."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input) return '';
            const chars = {
                'a': '𝗮', 'b': '𝗯', 'c': '𝗰', 'd': '𝗱', 'e': '𝗲', 'f': '𝗳', 'g': '𝗴', 'h': '𝗵', 'i': '𝗶',
                'j': '𝗷', 'k': '𝗸', 'l': '𝗹', 'm': '𝗺', 'n': '𝗻', 'o': '𝗼', 'p': '𝗽', 'q': '𝗾', 'r': '𝗿',
                's': '𝘀', 't': '𝘁', 'u': '𝘂', 'v': '𝘃', 'w': '𝘄', 'x': '𝘅', 'y': '𝘆', 'z': '𝘇',
                'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙', 'G': '𝗚', 'H': '𝗛', 'I': '𝗜',
                'J': '𝗝', 'K': '𝗞', 'L': '𝗟', 'M': '𝗠', 'N': '𝗡', 'O': '𝗢', 'P': '𝗣', 'Q': '𝗤', 'R': '𝗥',
                'S': '𝗦', 'T': '𝗧', 'U': '𝗨', 'V': '𝗩', 'W': '𝗪', 'X': '𝗫', 'Y': '𝗬', 'Z': '𝗭'
            };
            return input.split('').map(c => chars[c] || c).join('');
        }"""
    },
    {
        "filename": "case-converter.html",
        "tool_id": "case-converter",
        "h1": "Free Online Text Case Converter (AP Title, UPPER, lower, Sentence Case)",
        "badge": "Editorial & Formatting Tool",
        "title": "Online Text Case Converter | AP Title Case, UPPERCASE, lowercase",
        "meta_desc": "Convert text case online. Format AP Title Case, UPPERCASE, lowercase, Sentence case, and Capitalize Each Word instantly with client-side JavaScript.",
        "keywords": "title case converter, uppercase to lowercase, sentence case converter, AP title case tool online, capitalize each word generator",
        "summary": "Instantly transform text capitalization between AP Title Case, UPPERCASE, lowercase, Sentence case, and Capitalize Each Word. Standardize blog headlines, video titles, and editorial copy in seconds.",
        "icon": "fa-text-height",
        "color": "indigo",
        "category": "Social & Formatting",
        "instructions": [
            "Paste your text, headlines, or draft copy into the input area.",
            "Select your desired capitalization format (Title Case, UPPERCASE, lowercase, Sentence case).",
            "Click <strong>Copy Result</strong> to use your formatted text in articles, metadata, or spreadsheets."
        ],
        "tips": [
            "AP Title Case automatically preserves minor prepositions and conjunctions (and, but, for, in, of, on) in lowercase unless they start the sentence.",
            "Title Case headlines consistently achieve higher click-through rates on YouTube and Google Search."
        ],
        "deep_content": """
            <h3>Standardizing Capitalization for Editorial Publishing</h3>
            <p>Consistency in headline capitalization is a hallmark of professional publications. The Associated Press (AP) stylebook guidelines specify that nouns, pronouns, adjectives, verbs, and adverbs are capitalized, while conjunctions and short prepositions remain lowercase.</p>
        """,
        "faqs": [
            {
                "q": "What is AP Title Case format?",
                "a": "AP Title Case capitalizes the first word, last word, and all major words, keeping minor prepositions and conjunctions lowercase."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input) return '';
            const smallWords = /^(a|an|and|as|at|but|by|for|if|in|nor|of|on|or|so|the|to|up|yet)$/i;
            return input.split(/\\s+/).map((word, index, arr) => {
                const cleanWord = word.replace(/[^\\w]/g, '');
                if (index === 0 || index === arr.length - 1 || !smallWords.test(cleanWord)) {
                    return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
                }
                return word.toLowerCase();
            }).join(' ');
        }"""
    },
    {
        "filename": "speech-timer.html",
        "tool_id": "speech-timer",
        "h1": "Free Script-to-Speech Duration & Voiceover Speaking Time Calculator",
        "badge": "Video & Audio Production Tool",
        "title": "Script-to-Speech Duration Calculator | Speaking Time & WPM Timer",
        "meta_desc": "Calculate speaking time and voiceover duration from your script word count. Benchmark 130 WPM conversational, 160 WPM commercial, and 100 WPM dramatic pacing.",
        "keywords": "script speaking time calculator, words per minute timer, voiceover duration calculator, script to speech length, youtube video length estimator",
        "summary": "Convert script word counts into precise voiceover and speaking durations based on industry-standard WPM (Words Per Minute) benchmarks: 130 WPM (YouTube/Conversational), 160 WPM (Commercial/TikTok), and 100 WPM (Keynote/Dramatic).",
        "icon": "fa-stopwatch",
        "color": "amber",
        "category": "Video & Copywriting",
        "instructions": [
            "Paste your video script, speech, or podcast outline into the workspace.",
            "Review the calculated speaking durations across conversational, commercial, and slow pacing models.",
            "Adjust your script word count to fit strict video constraints (such as 60-second YouTube Shorts or 30-second commercial spots)."
        ],
        "tips": [
            "For a 60-second YouTube Short or Reel, keep your script strictly under 140–150 words to allow room for natural pauses and B-roll transitions.",
            "Add a 10% buffer time if your script includes sound effects, animations, or guest responses."
        ],
        "deep_content": """
            <h3>Writing for the Ear: Timing Voiceovers and Scripts</h3>
            <p>One of the most common pitfalls for creators is over-writing video scripts. When scripts exceed allotted platform limits, speakers are forced to rush their delivery, hurting audience retention. Calculating duration in advance ensures a natural, engaging vocal pace.</p>
        """,
        "faqs": [
            {
                "q": "What is the average conversational speaking rate for video?",
                "a": "The average speaking rate for conversational YouTube videos, tutorials, and podcasts is approximately 130 to 140 words per minute (WPM)."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input || !input.trim()) return '';
            const words = (input.match(/[\\w\\u00C0-\\u024F'-]+/g) || []).length;
            const convSec = Math.round((words / 130) * 60);
            const fastSec = Math.round((words / 160) * 60);
            const slowSec = Math.round((words / 100) * 60);
            const fmt = s => `${Math.floor(s / 60)}m ${s % 60}s`;
            return `--- SCRIPT DURATION BREAKDOWN ---
Total Words: ${words}

Conversational (130 WPM - YouTube / Podcasts): ${fmt(convSec)}
Fast-Paced (160 WPM - TikTok / Commercials): ${fmt(fastSec)}
Slow / Dramatic (100 WPM - Keynotes / Storytelling): ${fmt(slowSec)}`;
        }"""
    },
    {
        "filename": "clean-srt-subtitles.html",
        "tool_id": "clean-srt",
        "h1": "Free SRT Caption & Subtitle Cleaner (Convert Subtitles to Blog Text)",
        "badge": "Video Repurposing & Transcript Tool",
        "title": "SRT Caption Cleaner | Convert Subtitles into Clean Transcripts",
        "meta_desc": "Clean .SRT and WebVTT subtitle files into readable article text. Strip timecodes, sequence numbers, and formatting tags with zero server uploads.",
        "keywords": "SRT subtitle cleaner, convert srt to text, remove timecodes from srt, clean vtt captions online, video transcript extractor free",
        "summary": "Strip timecodes (00:00:00,000 --> 00:00:00,000), sequence line numbers, and HTML styling tags from raw subtitle files (.SRT and .VTT), leaving clean paragraph transcripts ready for blog publishing.",
        "icon": "fa-closed-captioning",
        "color": "indigo",
        "category": "Video & Copywriting",
        "instructions": [
            "Paste raw .SRT or WebVTT subtitle text exported from Premiere Pro, CapCut, Descript, or YouTube Studio.",
            "The cleaner automatically strips timecode headers and sequence numbers, reconstructing spoken sentences into clean paragraphs.",
            "Copy your cleaned transcript to repurpose video content into blog posts, newsletters, and social articles."
        ],
        "tips": [
            "Repurposing YouTube captions into written blog articles boosts organic search rankings with minimal extra writing effort.",
            "Combine this tool with the AI Artifact Cleaner to polish conversational transcripts into formal prose."
        ],
        "deep_content": """
            <h3>Repurposing Video Captions into Organic Search Traffic</h3>
            <p>Video transcripts contain rich spoken keyword combinations that search engine crawlers love. Extracting clean text from raw SRT files eliminates tedious manual timecode deletion and accelerates content repurposing workflows.</p>
        """,
        "faqs": [
            {
                "q": "Does this tool delete my spoken words?",
                "a": "No. The regex filter exclusively removes numeric timestamps and sequence identifiers, preserving 100% of your spoken words."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input) return '';
            return input
                .replace(/^WEBVTT[^\\n]*\\n+/i, '')
                .replace(/\\d{1,2}:\\d{2}:\\d{2}[,\\.]\\d{3}\\s*-->\\s*\\d{1,2}:\\d{2}:\\d{2}[,\\.]\\d{3}[^\\n]*/g, '')
                .replace(/^\\s*\\d+\\s*$/gm, '')
                .replace(/<\\/?[^>]+(>|$)/g, '')
                .replace(/\\{[^\\}]+\\}/g, '')
                .split(/\\r?\\n/).map(l => l.trim()).filter(Boolean).join('\\n\\n');
        }"""
    },
    {
        "filename": "online-teleprompter.html",
        "tool_id": "open-teleprompter",
        "h1": "Free Online Fullscreen Teleprompter (Mirror Mode & Speed Controls)",
        "badge": "Video Presentation & Prompter Tool",
        "title": "Online Fullscreen Teleprompter | Free Browser Video Script Prompter",
        "meta_desc": "Free online fullscreen teleprompter for creators and presenters. Smooth auto-scroll, speed controls, font resizing, and beam-splitter mirror rig mode.",
        "keywords": "online teleprompter free, fullscreen prompter browser, mirror teleprompter tool, video recording script prompter, smooth scroll prompter",
        "summary": "A distraction-free online teleprompter with smooth auto-scrolling, speed controls (1–10), font resizing (24–72px), guide target lines, and horizontal mirror mode for beam-splitter prompter rigs. Runs 100% in-browser.",
        "icon": "fa-chalkboard-user",
        "color": "indigo",
        "category": "Video & Copywriting",
        "instructions": [
            "Paste your speech or video script into the workspace.",
            "Click <strong>Launch Fullscreen Prompter</strong> to open the prompter viewport.",
            "Adjust scroll speed and font size with the top sliders, and press <kbd class=\"px-1 bg-slate-200 dark:bg-slate-700 rounded\">Spacebar</kbd> to play/pause smoothly as you record."
        ],
        "tips": [
            "Position your browser window as close as possible to your webcam or camera lens to maintain direct eye contact with your viewers.",
            "Enable 'Mirror Rig' mode when using an iPad or tablet under a 70/30 beam-splitter glass prompter rig."
        ],
        "deep_content": """
            <h3>Delivering Confident On-Camera Video Presentations</h3>
            <p>Using a teleprompter eliminates awkward memory pauses, reduces recording retakes, and ensures you cover all key talking points. An in-browser prompter provides professional studio capabilities without expensive dedicated software.</p>
        """,
        "faqs": [
            {
                "q": "What is Mirror Rig mode?",
                "a": "Mirror Rig mode flips the text horizontally so it appears normal when reflected on a 70/30 beam-splitter glass teleprompter mounted in front of a camera lens."
            }
        ],
        "js_transform": "function transform(input) { return input; }"
    },
    {
        "filename": "ai-text-cleaner.html",
        "tool_id": "clean-ai-artifacts",
        "h1": "Free AI Text Formatting & Clichéé Cleaner (Humanize ChatGPT Copy)",
        "badge": "AI Copy Sanitization Tool",
        "title": "AI Text Formatting & Clichéé Cleaner | Humanize ChatGPT & Claude Copy",
        "meta_desc": "Strip Markdown asterisks, excessive em-dashes, and robotic AI clichéés from ChatGPT and Claude copy. Prepare clean, professional text for publishing.",
        "keywords": "clean chatgpt text, remove markdown asterisks, humanize AI text layout, strip ai clichées, ai markdown sanitizer free",
        "summary": "Strip raw Markdown artifacts (double asterisks `**bold**`, backticks, heading hashes `###`) and robotic AI tropes (e.g. 'In today's fast-paced digital world...') from ChatGPT, Claude, and Gemini outputs.",
        "icon": "fa-broom",
        "color": "indigo",
        "category": "AI, SEO & Media",
        "instructions": [
            "Paste raw output generated by ChatGPT, Claude, Gemini, or DeepSeek into the input workspace.",
            "The cleaner strips markdown syntax, normalizes em-dashes, and humanizes clichéé opening phrases.",
            "Copy clean editorial copy ready for publishing in email newsletters, CMS editors, or documents."
        ],
        "tips": [
            "Raw markdown asterisks look broken in standard email clients like Mailchimp or Substack; strip them before sending.",
            "Removing clichéé opening phrases immediately boosts reader retention in the critical first 5 seconds."
        ],
        "deep_content": """
            <h3>Polishing AI Outputs for Professional Publishing</h3>
            <p>While generative AI tools accelerate content drafting, raw outputs frequently include telltale formatting artifacts and robotic verbal tropes that undermine credibility. Cleaning these artifacts ensures your published copy maintains an authoritative, human tone.</p>
        """,
        "faqs": [
            {
                "q": "Why should I remove Markdown asterisks from my text?",
                "a": "When copying AI text into email newsletters or CMS editors that do not parse Markdown, the double asterisks appear as raw symbols (**text**), creating an unpolished look."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input) return '';
            let cleaned = input
                .replace(/\\*\\*(.*?)\\*\\*/g, '$1')
                .replace(/\\*(.*?)\\*/g, '$1')
                .replace(/__(.*?)__/g, '$1')
                .replace(/`([^`]+)`/g, '$1')
                .replace(/^#{1,6}\\s+/gm, '')
                .replace(/^[-\\*]\\s+/gm, '• ')
                .replace(/\\s*—\\s*/g, ' — ')
                .replace(/\\s*–\\s*/g, ' - ');
            const clichées = [
                /^In today's fast-paced (world|digital landscape|environment),?\\s*/gim,
                /^In the fast-paced world of [^,\\n]+,?\\s*/gim,
                /^In a world where [^,\\n]+,?\\s*/gim,
                /^It's important to remember that\\s*/gim,
                /^First and foremost,?\\s*/gim
            ];
            clichées.forEach(c => cleaned = cleaned.replace(c, ''));
            return cleaned.trim();
        }"""
    },
    {
        "filename": "seo-slug-generator.html",
        "tool_id": "seo-slug",
        "h1": "Free SEO URL Slug Generator & Clean Permalink Builder",
        "badge": "Technical SEO & Permalinks",
        "title": "SEO URL Slug Generator | Clean Permalink & Link Builder Online",
        "meta_desc": "Generate clean, URL-friendly slugs for blog posts, products, and landing pages. Automatically lowercase text, remove accents, and format hyphenated permalinks.",
        "keywords": "URL slug generator, clean SEO link builder, remove special characters from URL, permalink generator, slugify online free",
        "summary": "Convert article titles and product names into clean, URL-friendly permalink slugs by converting text to lowercase, removing accents/diacritics, stripping special characters, and separating words with clean hyphens.",
        "icon": "fa-link",
        "color": "indigo",
        "category": "AI, SEO & Media",
        "instructions": [
            "Type or paste your blog title, headline, or product name into the input workspace.",
            "The generator produces a lowercase, hyphen-separated permalink slug instantly.",
            "Copy the slug into your WordPress, Shopify, Webflow, or Next.js URL settings."
        ],
        "tips": [
            "Always use hyphens (-) rather than underscores (_) because Google crawlers interpret hyphens as word spaces.",
            "Remove unnecessary stop words (a, an, the, and) to keep URLs concise and memorable."
        ],
        "deep_content": """
            <h3>Best Practices for Clean, Search-Engine-Friendly URL Slugs</h3>
            <p>A concise URL slug provides immediate context to both human searchers and search engine spiders. Short, keyword-rich permalinks achieve higher organic click-through rates and are easier to share across social media.</p>
        """,
        "faqs": [
            {
                "q": "Should I use hyphens or underscores in URLs?",
                "a": "Always use hyphens (-). Google explicitly recommends hyphens because its search algorithm interprets hyphens as spaces between words."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input) return '';
            return input
                .toLowerCase()
                .normalize('NFD')
                .replace(/[\\u0300-\\u036f]/g, '')
                .replace(/[^a-z0-9\\s-]/g, '')
                .trim()
                .replace(/\\s+/g, '-')
                .replace(/-+/g, '-');
        }"""
    },
    {
        "filename": "whitespace-trimmer.html",
        "tool_id": "clean-whitespace",
        "h1": "Free Whitespace & Trailing Space Trimmer Online",
        "badge": "Formatting & Whitespace Cleaner",
        "title": "Whitespace Trimmer & Cleaner | Remove Trailing Spaces Online",
        "meta_desc": "Trim trailing spaces, collapse redundant blank lines, and normalize whitespace in text and code files. 100% private in-browser tool.",
        "keywords": "whitespace trimmer, remove trailing spaces, collapse multiple blank lines, clean text spacing online, strip extra spaces free",
        "summary": "Remove invisible trailing whitespace from line ends, collapse multiple consecutive spaces into a single space, and standardize paragraph breaks for clean data and copy.",
        "icon": "fa-arrows-left-right-to-line",
        "color": "indigo",
        "category": "AI, SEO & Media",
        "instructions": [
            "Paste your unformatted code, tabular data, or copy into the workspace.",
            "The trimmer removes trailing spaces and normalizes multiple blank lines instantly.",
            "Click <strong>Copy Result</strong> to obtain clean, lightweight text."
        ],
        "tips": [
            "Clean up messy CSV and JSON exports by standardizing erratic indentation spacing.",
            "Stripping trailing whitespace reduces document byte size before saving or sending."
        ],
        "deep_content": """
            <h3>Normalizing Whitespace Across Documents</h3>
            <p>Irregular spaces and stray tabs often cause formatting errors across CMS editors, markdown compilers, and code repositories. Automated whitespace normalization ensures clean, consistent documents.</p>
        """,
        "faqs": [
            {
                "q": "What does this whitespace trimmer remove?",
                "a": "It removes spaces at line ends (trailing spaces), collapses multiple consecutive spaces into one space, and eliminates excessive blank lines."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input) return '';
            return input
                .split(/\\r?\\n/)
                .map(l => l.trimEnd().replace(/[ \\t]+/g, ' '))
                .join('\\n')
                .replace(/\\n{3,}/g, '\\n\\n')
                .trim();
        }"""
    },
    {
        "filename": "duplicate-line-filter.html",
        "tool_id": "remove-duplicates",
        "h1": "Free Duplicate Line Filter & List Deduplicator Online",
        "badge": "Data Processing & List Tool",
        "title": "Duplicate Line Filter | Deduplicate Lists, Keywords & Data Sets",
        "meta_desc": "Filter out duplicate lines from keyword lists, email rosters, and text sets. Sort alphabetically and deduplicate data with zero server uploads.",
        "keywords": "duplicate line remover, deduplicate list online, remove repeated lines, sort keyword list, clean email list deduplicator",
        "summary": "Scan multi-line keyword lists, URL rosters, email datasets, and text files to eliminate repeated duplicate entries and output a clean, unique set.",
        "icon": "fa-list-check",
        "color": "indigo",
        "category": "AI, SEO & Media",
        "instructions": [
            "Paste your list of keywords, URLs, or data lines into the workspace.",
            "The deduplication engine isolates unique entries and filters out all repeated lines.",
            "Copy your cleaned, deduplicated list in 1 click."
        ],
        "tips": [
            "Deduplicate merged keyword export lists from Ahrefs or SEMrush before building content clusters.",
            "Clean recipient rosters before importing to email marketing platforms."
        ],
        "deep_content": """
            <h3>Deduplicating High-Volume Data Sets in Client Memory</h3>
            <p>Managing large keyword lists or database exports requires fast list deduplication. Performing this operation locally in client memory guarantees privacy and instant results without uploading confidential business data to external servers.</p>
        """,
        "faqs": [
            {
                "q": "Is my data uploaded to any server?",
                "a": "No. All deduplication algorithms execute 100% client-side in your local browser sandbox."
            }
        ],
        "js_transform": """function transform(input) {
            if (!input) return '';
            const lines = input.split(/\\r?\\n/);
            const seen = new Set();
            const unique = [];
            lines.forEach(l => {
                const trimmed = l.trim();
                if (trimmed && !seen.has(trimmed)) {
                    seen.add(trimmed);
                    unique.push(trimmed);
                }
            });
            return unique.join('\\n');
        }"""
    }
]

def generate_page_html(tool):
    faqs_schema = [
        {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
        for f in tool["faqs"]
    ]
    schema_json = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebApplication",
                "name": tool["title"],
                "url": f"https://creatorkitstudio.pro/{tool['filename']}",
                "description": tool["meta_desc"],
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

    faqs_html = "".join([
        f"""<details class="group bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl p-4 transition [&_summary::-webkit-details-marker]:hidden" {'open' if i==0 else ''}>
            <summary class="flex items-center justify-between cursor-pointer font-semibold text-xs md:text-sm text-slate-900 dark:text-white">
                <span>{f['q']}</span>
                <span class="ml-2 text-slate-400 group-open:rotate-180 transition-transform">
                    <i class="fa-solid fa-chevron-down text-xs"></i>
                </span>
            </summary>
            <p class="mt-3 text-xs text-slate-600 dark:text-slate-400 leading-relaxed">{f['a']}</p>
        </details>"""
        for i, f in enumerate(tool["faqs"])
    ])

    instructions_html = "".join([f"<li>{step}</li>" for step in tool["instructions"]])
    tips_html = "".join([f"<li>{tip}</li>" for tip in tool["tips"]])

    # Related tools links
    other_tools = [t for t in TOOLS if t["filename"] != tool["filename"]][:6]
    related_html = "".join([
        f"""<a href="{ot['filename']}" class="p-3 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-dark-border hover:border-indigo-500 transition flex items-center gap-2.5 text-xs font-semibold text-slate-800 dark:text-slate-200 group">
            <i class="fa-solid {ot['icon']} text-indigo-500 group-hover:scale-110 transition-transform"></i>
            <span>{ot['badge'].split(' ')[0]} {ot['h1'].split(' ')[1] if len(ot['h1'].split(' ')) > 1 else 'Tool'}</span>
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
    <title>{tool['title']}</title>
    <meta name="description" content="{tool['meta_desc']}">
    <meta name="keywords" content="{tool['keywords']}">
    <meta name="author" content="CreatorKit Studio">
    <meta name="robots" content="index, follow">
    <meta name="google-site-verification" content="WM4c52x0WOHkjYTAqQMRLdBSMGOo3aG7IoGemVJVte8" />

    <!-- Force Cache-Busting Meta Tags -->
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="0" />

    <!-- Google AdSense Verification & Publisher Script -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5863857969717583" crossorigin="anonymous"></script>

    <!-- Open Graph / Meta -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{tool['title']}">
    <meta property="og:description" content="{tool['meta_desc']}">
    <meta property="og:url" content="https://creatorkitstudio.pro/{tool['filename']}">

    <!-- Favicon & App Icons -->
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🛠️</text></svg>">
    <link rel="icon" type="image/png" sizes="32x32" href="favicon.png">
    <link rel="apple-touch-icon" sizes="180x180" href="favicon.png">

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
                        dark: {{ bg: '#0f172a', surface: '#1e293b', border: '#334155', text: '#f8fafc', muted: '#94a3b8' }}
                    }}
                }}
            }}
        }}
    </script>

    <!-- FontAwesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css?v=2.2.0">
</head>
<body class="bg-slate-50 dark:bg-dark-bg text-slate-900 dark:text-dark-text antialiased min-h-screen flex flex-col font-['Inter',sans-serif]">

    <!-- Top Navbar with Deep Navigation Back to Main Suite -->
    <header class="bg-white dark:bg-dark-surface border-b border-slate-200 dark:border-dark-border sticky top-0 z-40 shadow-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <a href="index.html" class="flex items-center gap-2.5 group" title="Return to CreatorKit Studio Homepage">
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
                <a href="index.html#all" class="px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1.5">
                    <i class="fa-solid fa-globe text-indigo-500"></i> All 17 Tools
                </a>
                <a href="index.html#blogger" class="px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1.5">
                    <i class="fa-solid fa-feather text-amber-500"></i> Blogger Mode
                </a>
                <a href="index.html#creator" class="px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1.5">
                    <i class="fa-solid fa-video text-pink-500"></i> Creator Mode
                </a>
            </nav>

            <!-- Theme Toggle & Reset -->
            <div class="flex items-center gap-2">
                <button id="themeToggleBtn" aria-label="Toggle Theme" class="p-2 text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-lg transition">
                    <i id="themeIcon" class="fa-solid fa-moon text-base"></i>
                </button>
                <a href="index.html" class="px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm transition flex items-center gap-1.5">
                    <i class="fa-solid fa-table-cells"></i> <span class="hidden sm:inline">Suite Dashboard</span>
                </a>
            </div>
        </div>
    </header>

    <!-- Main Tool Container -->
    <main class="max-w-5xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8 space-y-8 flex-1">
        
        <!-- Breadcrumb Navigation -->
        <nav class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
            <a href="index.html" class="hover:text-indigo-500 transition">CreatorKit Studio</a>
            <i class="fa-solid fa-chevron-right text-[10px]"></i>
            <a href="index.html#all" class="hover:text-indigo-500 transition">{tool['category']}</a>
            <i class="fa-solid fa-chevron-right text-[10px]"></i>
            <span class="text-slate-800 dark:text-slate-200 font-semibold">{tool['h1'].split('(')[0].strip()}</span>
        </nav>

        <!-- Header Banner Ad Placeholder -->
        <div class="w-full">
            <div class="adsense-slot adsense-placeholder w-full rounded-xl border-2 border-dashed border-slate-300 dark:border-slate-700 flex flex-col items-center justify-center text-slate-400 dark:text-slate-500 text-xs gap-1 p-3 bg-white/40 dark:bg-slate-800/30 overflow-hidden text-center shadow-sm" style="min-height: 90px; height: 90px;">
                <span class="font-mono uppercase tracking-widest text-[10px] bg-slate-200 dark:bg-slate-700 px-2 py-0.5 rounded text-slate-600 dark:text-slate-300">Advertisement</span>
                <span class="flex items-center gap-1 font-mono text-[11px]"><i class="fa-brands fa-google text-indigo-500"></i> Google AdSense Leaderboard (Responsive)</span>
            </div>
        </div>

        <!-- Tool Heading Header -->
        <div class="space-y-2">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 border border-indigo-200/60 dark:border-indigo-800/40">
                <i class="fa-solid {tool['icon']}"></i> {tool['badge']}
            </div>
            <h1 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-slate-900 dark:text-white leading-tight">{tool['h1']}</h1>
            <p class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed max-w-3xl">{tool['summary']}</p>
        </div>

        <!-- Live Tool Workspace Card -->
        <div class="bg-white dark:bg-dark-surface rounded-2xl border border-slate-200 dark:border-dark-border p-5 sm:p-6 shadow-sm space-y-5">
            
            <!-- Live Analytics Strip -->
            <div class="grid grid-cols-3 sm:grid-cols-6 gap-2.5 pb-4 border-b border-slate-200 dark:border-dark-border text-center">
                <div class="p-2 bg-slate-50 dark:bg-slate-900 rounded-lg border border-slate-100 dark:border-dark-border/50">
                    <span class="text-[10px] uppercase font-semibold text-slate-400 block mb-0.5">Words</span>
                    <span id="statWords" class="text-base sm:text-lg font-bold font-mono text-slate-800 dark:text-slate-100">0</span>
                </div>
                <div class="p-2 bg-slate-50 dark:bg-slate-900 rounded-lg border border-slate-100 dark:border-dark-border/50">
                    <span class="text-[10px] uppercase font-semibold text-slate-400 block mb-0.5">Chars</span>
                    <span id="statChars" class="text-base sm:text-lg font-bold font-mono text-slate-800 dark:text-slate-100">0</span>
                </div>
                <div class="p-2 bg-slate-50 dark:bg-slate-900 rounded-lg border border-slate-100 dark:border-dark-border/50">
                    <span class="text-[10px] uppercase font-semibold text-slate-400 block mb-0.5">No Space</span>
                    <span id="statCharsNoSpace" class="text-base sm:text-lg font-bold font-mono text-slate-700 dark:text-slate-300">0</span>
                </div>
                <div class="p-2 bg-slate-50 dark:bg-slate-900 rounded-lg border border-slate-100 dark:border-dark-border/50">
                    <span class="text-[10px] uppercase font-semibold text-slate-400 block mb-0.5">Sentences</span>
                    <span id="statSentences" class="text-base sm:text-lg font-bold font-mono text-slate-700 dark:text-slate-300">0</span>
                </div>
                <div class="p-2 bg-slate-50 dark:bg-slate-900 rounded-lg border border-slate-100 dark:border-dark-border/50">
                    <span class="text-[10px] uppercase font-semibold text-slate-400 block mb-0.5">Reading</span>
                    <span id="statReadingTime" class="text-base sm:text-lg font-bold font-mono text-indigo-600 dark:text-indigo-400">0s</span>
                </div>
                <div class="p-2 bg-slate-50 dark:bg-slate-900 rounded-lg border border-slate-100 dark:border-dark-border/50">
                    <span class="text-[10px] uppercase font-semibold text-slate-400 block mb-0.5">Speech</span>
                    <span id="statSpeakingTime" class="text-base sm:text-lg font-bold font-mono text-amber-600 dark:text-amber-400">0s</span>
                </div>
            </div>

            <!-- Input / Output Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                
                <!-- Input Box -->
                <div class="space-y-2">
                    <div class="flex items-center justify-between">
                        <label for="toolInput" class="text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                            <i class="fa-solid fa-pen-to-square text-indigo-500"></i> Input Content
                        </label>
                        <button id="clearInputBtn" class="text-xs text-rose-500 hover:text-rose-600 transition font-medium">Clear</button>
                    </div>
                    <textarea id="toolInput" rows="9" placeholder="Type or paste your text here..." class="w-full p-3.5 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 font-sans resize-y custom-scrollbar transition"></textarea>
                </div>

                <!-- Output Box -->
                <div class="space-y-2">
                    <div class="flex items-center justify-between">
                        <label for="toolOutput" class="text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                            <i class="fa-solid fa-square-poll-vertical text-emerald-500"></i> Processed Output
                        </label>
                        <button id="copyBtn" class="px-3 py-1 text-xs font-semibold rounded-md bg-emerald-600 hover:bg-emerald-700 text-white shadow-sm transition flex items-center gap-1.5 active:scale-95">
                            <i class="fa-regular fa-copy"></i>
                            <span id="copyBtnText">Copy Result</span>
                        </button>
                    </div>
                    <textarea id="toolOutput" rows="9" readonly placeholder="Transformed output appears here automatically..." class="w-full p-3.5 text-sm bg-slate-100/80 dark:bg-slate-900/60 border border-slate-200 dark:border-dark-border rounded-xl text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none font-sans resize-y custom-scrollbar transition"></textarea>
                </div>

            </div>

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
                    <h3 class="text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400">Pro Tips & Best Practices:</h3>
                    <ul class="list-disc pl-5 text-xs text-slate-600 dark:text-slate-300 space-y-1.5 leading-relaxed">
                        {tips_html}
                    </ul>
                </div>
            </div>
        </section>

        <!-- In-Content Ad Banner -->
        <div class="w-full">
            <div class="adsense-slot adsense-placeholder w-full rounded-xl border-2 border-dashed border-slate-300 dark:border-slate-700 flex flex-col items-center justify-center text-slate-400 dark:text-slate-500 text-xs gap-1 p-3 bg-white/40 dark:bg-slate-800/30 overflow-hidden text-center shadow-sm" style="min-height: 90px; height: 90px;">
                <span class="font-mono uppercase tracking-widest text-[10px] bg-slate-200 dark:bg-slate-700 px-2 py-0.5 rounded text-slate-600 dark:text-slate-300">Advertisement</span>
                <span class="flex items-center gap-1 font-mono text-[11px]"><i class="fa-brands fa-google text-indigo-500"></i> Google AdSense Responsive In-Content Banner</span>
            </div>
        </div>

        <!-- Deep Educational Guide Article -->
        <article class="prose prose-slate dark:prose-invert max-w-none bg-white dark:bg-dark-surface p-6 sm:p-8 rounded-2xl border border-slate-200 dark:border-dark-border shadow-sm space-y-4 text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
            <h2 class="text-xl font-bold text-slate-900 dark:text-white">Comprehensive Guide: {tool['h1'].split('(')[0].strip()}</h2>
            {tool['deep_content']}
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

        <!-- Related Creator Tools Grid -->
        <section class="space-y-3">
            <h2 class="text-sm font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Explore More Free Creator Tools:</h2>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
                {related_html}
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-white dark:bg-dark-surface border-t border-slate-200 dark:border-dark-border py-8 px-4 sm:px-6 lg:px-8 text-xs text-slate-500 dark:text-slate-400">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
            <div>
                <span class="font-bold text-slate-800 dark:text-slate-200">CreatorKit Studio</span> &copy; 2026. Free 100% Client-Side Web Utilities.
            </div>
            <div class="flex items-center gap-5 font-medium">
                <a href="index.html#all" class="hover:text-indigo-500">All Tools</a>
                <a href="index.html#blogger" class="hover:text-indigo-500">Blogger Suite</a>
                <a href="index.html#creator" class="hover:text-indigo-500">Creator Suite</a>
            </div>
        </div>
    </footer>

    <!-- Dedicated Tool Script -->
    <script>
        {tool['js_transform']}

        const inputEl = document.getElementById('toolInput');
        const outputEl = document.getElementById('toolOutput');
        const copyBtn = document.getElementById('copyBtn');
        const copyBtnText = document.getElementById('copyBtnText');
        const clearBtn = document.getElementById('clearInputBtn');

        function updateAnalytics(text) {{
            const words = (text.match(/[\\w\\u00C0-\\u024F'-]+/g) || []).length;
            const chars = text.length;
            const charsNoSpace = text.replace(/\\s/g, '').length;
            const sentences = (text.match(/[^.!?]+[.!?]+(\\s|$)/g) || [1]).length;
            const readSec = Math.round((words / 200) * 60);
            const speakSec = Math.round((words / 130) * 60);

            document.getElementById('statWords').textContent = words.toLocaleString();
            document.getElementById('statChars').textContent = chars.toLocaleString();
            document.getElementById('statCharsNoSpace').textContent = charsNoSpace.toLocaleString();
            document.getElementById('statSentences').textContent = (text.trim() ? sentences : 0).toLocaleString();
            document.getElementById('statReadingTime').textContent = readSec > 60 ? `${{Math.floor(readSec/60)}}m ${{readSec%60}}s` : `${{readSec}}s`;
            document.getElementById('statSpeakingTime').textContent = speakSec > 60 ? `${{Math.floor(speakSec/60)}}m ${{speakSec%60}}s` : `${{speakSec}}s`;
        }}

        function process() {{
            const val = inputEl.value;
            updateAnalytics(val);
            outputEl.value = transform(val);
        }}

        inputEl.addEventListener('input', process);
        clearBtn.addEventListener('click', () => {{
            inputEl.value = '';
            process();
        }});

        copyBtn.addEventListener('click', async () => {{
            if (!outputEl.value) return;
            try {{
                await navigator.clipboard.writeText(outputEl.value);
                copyBtnText.textContent = 'Copied!';
                copyBtn.classList.replace('bg-emerald-600', 'bg-indigo-600');
                setTimeout(() => {{
                    copyBtnText.textContent = 'Copy Result';
                    copyBtn.classList.replace('bg-indigo-600', 'bg-emerald-600');
                }}, 1500);
            }} catch (err) {{
                outputEl.select();
                document.execCommand('copy');
            }}
        }});

        // Theme Toggle
        const themeBtn = document.getElementById('themeToggleBtn');
        const themeIcon = document.getElementById('themeIcon');
        themeBtn.addEventListener('click', () => {{
            const isDark = document.documentElement.classList.toggle('dark');
            localStorage.setItem('creatorkit_theme', isDark ? 'dark' : 'light');
            themeIcon.className = isDark ? 'fa-solid fa-sun text-base text-amber-400' : 'fa-solid fa-moon text-base text-slate-600';
        }});

        // Load saved theme
        if (localStorage.getItem('creatorkit_theme') === 'light') {{
            document.documentElement.classList.remove('dark');
            themeIcon.className = 'fa-solid fa-moon text-base text-slate-600';
        }} else {{
            document.documentElement.classList.add('dark');
            themeIcon.className = 'fa-solid fa-sun text-base text-amber-400';
        }}
    </script>
</body>
</html>
"""

def generate_sitemap():
    base = "https://creatorkitstudio.pro/"
    entries = [
        f"""    <url>
        <loc>{base}</loc>
        <lastmod>2026-08-30</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>""",
        f"""    <url>
        <loc>{base}#all</loc>
        <lastmod>2026-08-30</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>""",
        f"""    <url>
        <loc>{base}#blogger</loc>
        <lastmod>2026-08-30</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>""",
        f"""    <url>
        <loc>{base}#creator</loc>
        <lastmod>2026-08-30</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>"""
    ]

    for tool in TOOLS:
        entries.append(f"""    <url>
        <loc>{base}{tool['filename']}</loc>
        <lastmod>2026-08-30</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.85</priority>
    </url>""")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    
{chr(10).join(entries)}

</urlset>"""

def main():
    root = r"d:\all in one tools website"
    print("Generating dedicated standalone SEO pages...")
    for tool in TOOLS:
        filepath = os.path.join(root, tool["filename"])
        html_content = generate_page_html(tool)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Created {tool['filename']} ({len(html_content)} bytes)")

    sitemap_path = os.path.join(root, "sitemap.xml")
    sitemap_content = generate_sitemap()
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print(f"Updated sitemap.xml with {len(TOOLS) + 4} URLs")

if __name__ == "__main__":
    main()
