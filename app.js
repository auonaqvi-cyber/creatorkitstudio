/**
 * CreatorKit Studio - High-Performance Client-Side Creator Suite
 * 100% Browser Execution - Zero Data Upload - AdSense & SEO Optimized
 */

(function () {
    'use strict';

    // ==========================================
    // STATE & DOM CACHE
    // ==========================================
    const state = {
        activeTool: 'fix-line-breaks',
        fancyStyle: 'bold-sans',
        caseFormat: 'title',
        teleprompter: {
            isPlaying: false,
            speed: 3,
            fontSize: 44,
            isMirrored: false,
            animationFrameId: null
        }
    };

    // DOM Elements
    const elements = {
        // Metadata & Schema
        pageTitle: document.getElementById('pageTitle'),
        pageMetaDescription: document.getElementById('pageMetaDescription'),
        ogTitle: document.getElementById('ogTitle'),
        ogDescription: document.getElementById('ogDescription'),
        faqSchema: document.getElementById('faqSchema'),
        dynamicSeoGuide: document.getElementById('dynamicSeoGuide'),

        // Inputs & Outputs
        mainInput: document.getElementById('mainInput'),
        mainOutput: document.getElementById('mainOutput'),
        dynamicToolOptions: document.getElementById('dynamicToolOptions'),
        autoSaveBadge: document.getElementById('autoSaveBadge'),
        outputChangeBadge: document.getElementById('outputChangeBadge'),
        copyFeedbackBadge: document.getElementById('copyFeedbackBadge'),

        // Action Buttons
        copyOutputBtn: document.getElementById('copyOutputBtn'),
        sendToInputBtn: document.getElementById('sendToInputBtn'),
        downloadOutputBtn: document.getElementById('downloadOutputBtn'),
        pasteBtn: document.getElementById('pasteBtn'),
        clearInputBtn: document.getElementById('clearInputBtn'),
        clearAllBtn: document.getElementById('clearAllBtn'),

        // Search & Filters
        headerToolSearch: document.getElementById('headerToolSearch'),
        sidebarToolSearch: document.getElementById('sidebarToolSearch'),
        toolsListContainer: document.getElementById('toolsListContainer'),
        toolCountBadge: document.getElementById('toolCountBadge'),

        // Analytics
        statWords: document.getElementById('statWords'),
        statChars: document.getElementById('statChars'),
        statCharsNoSpace: document.getElementById('statCharsNoSpace'),
        statSentences: document.getElementById('statSentences'),
        statParagraphs: document.getElementById('statParagraphs'),
        statLines: document.getElementById('statLines'),
        statReadingTime: document.getElementById('statReadingTime'),
        statSpeakingTime: document.getElementById('statSpeakingTime'),

        // Theme Toggle
        themeToggleBtn: document.getElementById('themeToggleBtn'),
        themeIcon: document.getElementById('themeIcon'),

        // Teleprompter Modal Elements
        teleprompterModal: document.getElementById('teleprompterModal'),
        teleprompterLaunchBtn: document.getElementById('teleprompterLaunchBtn'),
        tpViewport: document.getElementById('tpViewport'),
        tpContent: document.getElementById('tpContent'),
        tpPlayPauseBtn: document.getElementById('tpPlayPauseBtn'),
        tpPlayStatusText: document.getElementById('tpPlayStatusText'),
        tpResetBtn: document.getElementById('tpResetBtn'),
        tpSpeedSlider: document.getElementById('tpSpeedSlider'),
        tpSpeedValue: document.getElementById('tpSpeedValue'),
        tpFontSlider: document.getElementById('tpFontSlider'),
        tpFontValue: document.getElementById('tpFontValue'),
        tpMirrorBtn: document.getElementById('tpMirrorBtn'),
        tpCloseBtn: document.getElementById('tpCloseBtn'),

        // Legal Modals Elements
        legalModal: document.getElementById('legalModal'),
        legalModalTitle: document.getElementById('legalModalTitle'),
        legalModalBody: document.getElementById('legalModalBody'),
        closeLegalModalBtn: document.getElementById('closeLegalModalBtn'),
        closeLegalModalFooterBtn: document.getElementById('closeLegalModalFooterBtn'),
        openAboutBtn: document.getElementById('openAboutBtn'),
        openPrivacyBtn: document.getElementById('openPrivacyBtn'),
        openTermsBtn: document.getElementById('openTermsBtn'),
        openContactBtn: document.getElementById('openContactBtn'),

        // Sample Loaders
        sampleSrtBtn: document.getElementById('sampleSrtBtn'),
        sampleAiBtn: document.getElementById('sampleAiBtn'),
        sampleSocialBtn: document.getElementById('sampleSocialBtn'),
        sampleScriptBtn: document.getElementById('sampleScriptBtn'),

        // Toast Container
        toastContainer: document.getElementById('toastContainer')
    };

    // ==========================================
    // UNICODE MAPS FOR FANCY TEXT GENERATOR
    // ==========================================
    const UNICODE_FONTS = {
        'bold-sans': {
            chars: '𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭0123456789',
            digits: '𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵'
        },
        'bold-serif': {
            chars: '𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙0123456789',
            digits: '𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗'
        },
        'italic': {
            chars: '𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡0123456789',
            digits: '0123456789'
        },
        'bubble': {
            chars: 'ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ0①②③④⑤⑥⑦⑧⑨',
            digits: '⓪①②③④⑤⑥⑦⑧⑨'
        },
        'monospace': {
            chars: '𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕ⓜⓝⓞ𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉0123456789',
            digits: '𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿'
        },
        'gothic': {
            chars: '𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ0123456789',
            digits: '0123456789'
        }
    };
    const PLAIN_ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';

    // ==========================================
    // SAMPLE DATASETS FOR DEMONSTRATION
    // ==========================================
    const SAMPLE_DATA = {
        srt: `1
00:00:01,200 --> 00:00:04,500
Welcome back to CreatorKit Studio!

2
00:00:04,800 --> 00:00:08,150
Today we are showing you how to clean <b>SRT subtitles</b> instantly.

3
00:00:08,400 --> 00:00:12,900
No more manual timestamp deletion or broken line breaks in your video scripts!`,

        ai: `**In today's fast-paced digital world**, creating high-converting content is more important than ever. 

In this article, we delve into the tapestry of modern social algorithms — unlocking growth for creators.

**Key Takeaways:**
* Point 1: Always format clean captions.
* Point 2: Avoid cliché AI phrases like "In conclusion" or "delve into".

In conclusion, having client-side creator tools elevates your workflow!`,

        social: `Stop struggling with cramped Instagram and LinkedIn captions! 

When you post multiple paragraphs on social media, the mobile app often squishes everything together.

With CreatorKit Studio:
1. Write your draft with clean double spacing.
2. Hit "Fix Paragraphs".
3. Paste directly to Instagram, Threads, or LinkedIn.

#contentcreator #marketing #socialmediatips #copywriting #growthhacks #creatorlife`,

        script: `Have you ever wondered why top creators post every single day without burning out? 

The secret isn't working 14 hours a day. It's having an automated system for writing, cleaning, and pacing your voiceovers.

At a standard conversational pace of 130 words per minute, this 65-word script takes precisely 30 seconds to record for a viral TikTok or YouTube Short. Clean, punchy, and straight to the point!`
    };

    // ==========================================
    // MODULAR UTILITY FUNCTIONS
    // ==========================================

    // 1. Line Break & Paragraph Fixer for Instagram/LinkedIn
    function fixLineBreaks(text) {
        if (!text) return '';
        const lines = text.split(/\r?\n/);
        const fixedLines = lines.map((line) => {
            if (line.trim() === '') {
                return '\u200B'; // Zero-width space preserves the blank line
            }
            return line;
        });
        return fixedLines.join('\n');
    }

    // 2. Fancy Unicode Text Generator
    function generateFancyText(text, style = 'bold-sans') {
        if (!text) return '';
        const fontMap = UNICODE_FONTS[style] || UNICODE_FONTS['bold-sans'];
        const fontChars = Array.from(fontMap.chars);
        const plainChars = Array.from(PLAIN_ALPHABET);

        let result = '';
        for (const char of text) {
            const index = plainChars.indexOf(char);
            if (index !== -1 && fontChars[index]) {
                result += fontChars[index];
            } else {
                result += char;
            }
        }
        return result;
    }

    // 3. Hashtag Extractor & Cleaner
    function cleanHashtags(text, maxCount = 30) {
        if (!text) return '';
        const matches = text.match(/#[a-zA-Z0-9_\u00C0-\u024F\u0400-\u04FF]+/g) || [];
        const seen = new Set();
        const uniqueTags = [];

        for (const tag of matches) {
            const lower = tag.toLowerCase();
            if (!seen.has(lower)) {
                seen.add(lower);
                uniqueTags.push(tag);
            }
        }

        const limitedTags = uniqueTags.slice(0, maxCount);
        return limitedTags.join(' ');
    }

    // 4. Case Converter
    function convertCase(text, format = 'title') {
        if (!text) return '';
        switch (format) {
            case 'upper':
                return text.toUpperCase();
            case 'lower':
                return text.toLowerCase();
            case 'sentence':
                return text.toLowerCase().replace(/(^\s*\w|[.!?]\s+\w)/g, (c) => c.toUpperCase());
            case 'capitalize':
                return text.replace(/\b\w/g, (c) => c.toUpperCase());
            case 'title': {
                const smallWords = /^(a|an|and|as|at|but|by|for|if|in|nor|of|on|or|so|the|to|up|yet)$/i;
                return text.split(/\s+/).map((word, index, arr) => {
                    const cleanWord = word.replace(/[^\w]/g, '');
                    if (index === 0 || index === arr.length - 1 || !smallWords.test(cleanWord)) {
                        return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
                    }
                    return word.toLowerCase();
                }).join(' ');
            }
            case 'camel':
                return text.toLowerCase().replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase());
            default:
                return text;
        }
    }

    // 5. SRT Caption Cleaner
    function cleanSRT(srtContent) {
        if (!srtContent) return '';
        let cleaned = srtContent
            .replace(/^WEBVTT[^\n]*\n+/i, '')
            .replace(/\d{1,2}:\d{2}:\d{2}[,\.]\d{3}\s*-->\s*\d{1,2}:\d{2}:\d{2}[,\.]\d{3}[^\n]*/g, '')
            .replace(/^\s*\d+\s*$/gm, '')
            .replace(/<\/?[^>]+(>|$)/g, '')
            .replace(/\{[^\}]+\}/g, '');

        const lines = cleaned.split(/\r?\n/).map(l => l.trim()).filter(Boolean);
        return lines.join('\n\n');
    }

    // 6. Script Speaking Duration Calculator
    function calculateSpeakingTimeDetails(text, wpm = 130) {
        const words = countWords(text);
        const totalSeconds = Math.round((words / wpm) * 60);
        const minutes = Math.floor(totalSeconds / 60);
        const seconds = totalSeconds % 60;
        return {
            words,
            totalSeconds,
            minutes,
            seconds,
            formatted: minutes > 0 ? `${minutes}m ${seconds}s` : `${seconds}s`
        };
    }

    // 7. AI Formatting & Cliché Cleaner
    function cleanAIArtifacts(text) {
        if (!text) return '';
        let cleaned = text;

        cleaned = cleaned
            .replace(/\*\*(.*?)\*\*/g, '$1')
            .replace(/\*(.*?)\*/g, '$1')
            .replace(/__(.*?)__/g, '$1')
            .replace(/`([^`]+)`/g, '$1')
            .replace(/^#{1,6}\s+/gm, '')
            .replace(/^[-\*]\s+/gm, '• ');

        cleaned = cleaned
            .replace(/\s*—\s*/g, ' — ')
            .replace(/\s*–\s*/g, ' - ');

        const cliches = [
            /^In today's fast-paced (world|digital landscape|environment),?\s*/gim,
            /^In the fast-paced world of [^,\n]+,?\s*/gim,
            /^In a world where [^,\n]+,?\s*/gim,
            /^In conclusion,?\s*/gim,
            /^To sum up,?\s*/gim,
            /^Without further ado,?\s*/gim,
            /^Let's dive in:?\s*/gim,
            /^Let's delve into [^,\n]+:?\s*/gim,
            /^It is important to remember that\s*/gim,
            /^It's worth noting that\s*/gim,
            /^As an AI language model,?\s*/gim,
            /^Certainly! Here is [^:\n]+:?\s*/gim,
            /^Sure thing! Here's [^:\n]+:?\s*/gim
        ];

        for (const regex of cliches) {
            cleaned = cleaned.replace(regex, '');
        }

        return cleaned.trim();
    }

    // 8. SEO Slug Generator
    function generateSEOSlug(text) {
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

    // 9. Whitespace Trimmer
    function cleanWhitespace(text) {
        if (!text) return '';
        return text
            .split(/\r?\n/)
            .map(line => line.replace(/[ \t]+/g, ' ').trim())
            .filter((line, i, arr) => !(line === '' && arr[i - 1] === ''))
            .join('\n')
            .trim();
    }

    // 10. Duplicate Line Filter
    function removeDuplicateLines(text) {
        if (!text) return '';
        const lines = text.split(/\r?\n/);
        const seen = new Set();
        const unique = [];

        for (const line of lines) {
            const trimmed = line.trim();
            if (trimmed === '' || !seen.has(trimmed)) {
                if (trimmed !== '') seen.add(trimmed);
                unique.push(line);
            }
        }
        return unique.join('\n');
    }

    // ==========================================
    // TEXT ANALYTICS ENGINE
    // ==========================================
    function countWords(str) {
        if (!str || str.trim() === '') return 0;
        const matches = str.trim().match(/[\w\u00C0-\u024F\u0400-\u04FF'-]+/g);
        return matches ? matches.length : 0;
    }

    function updateAnalytics(text) {
        const words = countWords(text);
        const chars = text.length;
        const charsNoSpace = text.replace(/\s/g, '').length;
        const sentences = text.trim() ? (text.match(/[^.!?]+[.!?]+(\s|$)/g) || [1]).length : 0;
        const paragraphs = text.trim() ? text.split(/\n+/).filter(p => p.trim().length > 0).length : 0;
        const lines = text ? text.split(/\r?\n/).length : 0;

        const readingSec = Math.round((words / 200) * 60);
        const readingMin = Math.floor(readingSec / 60);
        const readingRemSec = readingSec % 60;
        const readingDisplay = readingMin > 0 ? `${readingMin}m ${readingRemSec}s` : `${readingSec}s`;

        const speakingSec = Math.round((words / 130) * 60);
        const speakingMin = Math.floor(speakingSec / 60);
        const speakingRemSec = speakingSec % 60;
        const speakingDisplay = speakingMin > 0 ? `${speakingMin}m ${speakingRemSec}s` : `${speakingSec}s`;

        elements.statWords.textContent = words.toLocaleString();
        elements.statChars.textContent = chars.toLocaleString();
        elements.statCharsNoSpace.textContent = charsNoSpace.toLocaleString();
        elements.statSentences.textContent = sentences.toLocaleString();
        elements.statParagraphs.textContent = paragraphs.toLocaleString();
        elements.statLines.textContent = lines.toLocaleString();
        elements.statReadingTime.textContent = readingDisplay;
        elements.statSpeakingTime.textContent = speakingDisplay;
    }

    // ==========================================
    // DYNAMIC SEO GUIDE & SCHEMA.ORG RENDERER
    // ==========================================
    function renderSeoGuide(toolId) {
        if (typeof SEO_GUIDES === 'undefined') return;
        const guide = SEO_GUIDES[toolId] || SEO_GUIDES['fix-line-breaks'];
        if (!guide) return;

        // Update Title and Meta Tags
        if (elements.pageTitle) elements.pageTitle.textContent = guide.title;
        if (elements.pageMetaDescription) elements.pageMetaDescription.setAttribute('content', guide.metaDescription);
        if (elements.ogTitle) elements.ogTitle.setAttribute('content', guide.title);
        if (elements.ogDescription) elements.ogDescription.setAttribute('content', guide.metaDescription);

        // Update Schema.org JSON-LD FAQPage
        if (elements.faqSchema && guide.faqs) {
            const schemaData = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": guide.faqs.map(faq => ({
                    "@type": "Question",
                    "name": faq.q,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": faq.a
                    }
                }))
            };
            elements.faqSchema.textContent = JSON.stringify(schemaData, null, 2);
        }

        // Render HTML Content & FAQ Accordions
        const keywordsPills = (guide.keywords || []).map(kw => 
            `<span class="px-2 py-0.5 rounded text-[11px] font-medium bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-dark-border">${kw}</span>`
        ).join(' ');

        const faqsHtml = (guide.faqs || []).map((faq, index) => `
            <details class="group bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl p-4 transition [&_summary::-webkit-details-marker]:hidden" ${index === 0 ? 'open' : ''}>
                <summary class="flex items-center justify-between cursor-pointer font-semibold text-xs md:text-sm text-slate-900 dark:text-white">
                    <span>${faq.q}</span>
                    <span class="ml-2 text-slate-400 group-open:rotate-180 transition-transform">
                        <i class="fa-solid fa-chevron-down text-xs"></i>
                    </span>
                </summary>
                <p class="mt-3 text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                    ${faq.a}
                </p>
            </details>
        `).join('');

        elements.dynamicSeoGuide.innerHTML = `
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-200 dark:border-dark-border pb-3">
                    <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 border border-indigo-200/60 dark:border-indigo-800/40">
                        <i class="fa-solid fa-book-open"></i> ${guide.badge || 'Creator Educational Guide'}
                    </span>
                    <div class="flex flex-wrap gap-1.5">
                        ${keywordsPills}
                    </div>
                </div>

                <h2 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">
                    ${guide.h2}
                </h2>

                <div class="guide-body">
                    ${guide.contentHtml}
                </div>

                <!-- Structured FAQ Accordions -->
                <div class="pt-6 border-t border-slate-200 dark:border-dark-border space-y-3">
                    <h3 class="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2 mb-3">
                        <i class="fa-solid fa-circle-question text-indigo-500"></i> Frequently Asked Questions & Best Practices
                    </h3>
                    <div class="space-y-2.5">
                        ${faqsHtml}
                    </div>
                </div>
            </div>
        `;
    }

    // ==========================================
    // WORKSPACE PROCESSING ENGINE
    // ==========================================
    function processActiveTool() {
        const inputText = elements.mainInput.value;
        let outputText = '';

        switch (state.activeTool) {
            case 'fix-line-breaks':
                outputText = fixLineBreaks(inputText);
                break;
            case 'fancy-text':
                outputText = generateFancyText(inputText, state.fancyStyle);
                break;
            case 'clean-hashtags':
                outputText = cleanHashtags(inputText, 30);
                break;
            case 'case-converter':
                outputText = convertCase(inputText, state.caseFormat);
                break;
            case 'clean-srt':
                outputText = cleanSRT(inputText);
                break;
            case 'speech-timer': {
                const details = calculateSpeakingTimeDetails(inputText, 130);
                outputText = `📊 SCRIPT SPEAKING DURATION BREAKDOWN:\n` +
                    `--------------------------------------\n` +
                    `• Total Word Count: ${details.words} words\n` +
                    `• Conversational Voiceover (130 WPM): ${details.formatted} (${details.totalSeconds} total seconds)\n` +
                    `• Fast Commercial / TikTok Pacing (160 WPM): ${Math.round((details.words / 160) * 60)} seconds\n` +
                    `• Slow Guided / Meditation Pacing (100 WPM): ${Math.round((details.words / 100) * 60)} seconds\n\n` +
                    `Script Clean Content:\n` +
                    `--------------------------------------\n` +
                    inputText;
                break;
            }
            case 'clean-ai-artifacts':
                outputText = cleanAIArtifacts(inputText);
                break;
            case 'seo-slug':
                outputText = generateSEOSlug(inputText);
                break;
            case 'clean-whitespace':
                outputText = cleanWhitespace(inputText);
                break;
            case 'remove-duplicates':
                outputText = removeDuplicateLines(inputText);
                break;
            case 'open-teleprompter':
                openTeleprompter();
                outputText = inputText;
                break;
            default:
                outputText = inputText;
        }

        elements.mainOutput.value = outputText;

        // Feedback badge
        if (outputText && outputText !== inputText) {
            elements.outputChangeBadge.classList.remove('hidden');
            elements.outputChangeBadge.textContent = 'Transformed ✓';
        } else {
            elements.outputChangeBadge.classList.add('hidden');
        }
    }

    // Render dynamic sub-options for active tool
    function renderDynamicToolOptions(toolAction) {
        if (toolAction === 'fancy-text') {
            elements.dynamicToolOptions.classList.remove('hidden');
            elements.dynamicToolOptions.innerHTML = `
                <div class="flex flex-wrap items-center gap-3">
                    <span class="font-semibold text-slate-700 dark:text-slate-300">Choose Font Style:</span>
                    <div class="flex flex-wrap gap-1.5" id="fancyStyleOptions">
                        <button type="button" data-style="bold-sans" class="px-2.5 py-1 rounded border text-xs font-semibold ${state.fancyStyle === 'bold-sans' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'}">𝗕𝗼𝗹𝗱 𝗦𝗮𝗻𝘀</button>
                        <button type="button" data-style="bold-serif" class="px-2.5 py-1 rounded border text-xs font-semibold ${state.fancyStyle === 'bold-serif' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'}">𝐁𝐨𝐥𝐝 𝐒𝐞𝐫𝐢𝐟</button>
                        <button type="button" data-style="italic" class="px-2.5 py-1 rounded border text-xs font-semibold ${state.fancyStyle === 'italic' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'}">𝘐𝘵𝘢𝘭𝘪𝘤</button>
                        <button type="button" data-style="bubble" class="px-2.5 py-1 rounded border text-xs font-semibold ${state.fancyStyle === 'bubble' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'}">ⓑⓤⓑⓑⓛⓔ</button>
                        <button type="button" data-style="monospace" class="px-2.5 py-1 rounded border text-xs font-semibold ${state.fancyStyle === 'monospace' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'}">𝚖𝚘𝚗𝚘</button>
                        <button type="button" data-style="gothic" class="px-2.5 py-1 rounded border text-xs font-semibold ${state.fancyStyle === 'gothic' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'}">𝔊𝔬𝔱𝔥𝔦𝔠</button>
                    </div>
                </div>
            `;

            const styleBtns = elements.dynamicToolOptions.querySelectorAll('#fancyStyleOptions button');
            styleBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    state.fancyStyle = btn.dataset.style;
                    renderDynamicToolOptions('fancy-text');
                    processActiveTool();
                });
            });
        } else if (toolAction === 'case-converter') {
            elements.dynamicToolOptions.classList.remove('hidden');
            elements.dynamicToolOptions.innerHTML = `
                <div class="flex flex-wrap items-center gap-3">
                    <span class="font-semibold text-slate-700 dark:text-slate-300">Convert Format:</span>
                    <div class="flex flex-wrap gap-1.5" id="caseFormatOptions">
                        <button type="button" data-case="title" class="px-2.5 py-1 rounded border text-xs font-semibold ${state.caseFormat === 'title' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'}">Title Case</button>
                        <button type="button" data-case="sentence" class="px-2.5 py-1 rounded border text-xs font-semibold ${state.caseFormat === 'sentence' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'}">Sentence case</button>
                        <button type="button" data-case="upper" class="px-2.5 py-1 rounded border text-xs font-semibold ${state.caseFormat === 'upper' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'}">UPPERCASE</button>
                        <button type="button" data-case="lower" class="px-2.5 py-1 rounded border text-xs font-semibold ${state.caseFormat === 'lower' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'}">lowercase</button>
                        <button type="button" data-case="capitalize" class="px-2.5 py-1 rounded border text-xs font-semibold ${state.caseFormat === 'capitalize' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'}">Capitalize Each</button>
                    </div>
                </div>
            `;

            const caseBtns = elements.dynamicToolOptions.querySelectorAll('#caseFormatOptions button');
            caseBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    state.caseFormat = btn.dataset.case;
                    renderDynamicToolOptions('case-converter');
                    processActiveTool();
                });
            });
        } else {
            elements.dynamicToolOptions.classList.add('hidden');
            elements.dynamicToolOptions.innerHTML = '';
        }
    }

    // Set active tool from UI & Hash Route
    function setActiveTool(toolAction, updateHash = true) {
        state.activeTool = toolAction;

        if (updateHash && window.location.hash !== `#${toolAction}`) {
            history.pushState(null, '', `#${toolAction}`);
        }

        // Update sidebar tool active states
        document.querySelectorAll('.tool-btn').forEach(btn => {
            if (btn.dataset.action === toolAction) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // Update quick action buttons
        document.querySelectorAll('.action-btn').forEach(btn => {
            if (btn.dataset.action === toolAction) {
                btn.classList.add('bg-indigo-600', 'text-white');
                btn.classList.remove('bg-indigo-50', 'dark:bg-indigo-950/60', 'text-indigo-700', 'dark:text-indigo-300');
            } else {
                btn.classList.remove('bg-indigo-600', 'text-white');
                btn.classList.add('bg-indigo-50', 'dark:bg-indigo-950/60', 'text-indigo-700', 'dark:text-indigo-300');
            }
        });

        renderDynamicToolOptions(toolAction);
        processActiveTool();
        renderSeoGuide(toolAction);

        // Auto-close mobile accordion drawer when a tool is selected on mobile (< 768px)
        if (window.innerWidth < 768) {
            const drawer = document.getElementById('mobileToolDrawer');
            if (drawer && drawer.hasAttribute('open')) {
                drawer.removeAttribute('open');
            }
        }
    }

    // ==========================================
    // TELEPROMPTER CONTROLLER
    // ==========================================
    function openTeleprompter() {
        const text = elements.mainInput.value.trim() || 'Please type or paste your script in the workspace input box to begin reading on the teleprompter.';
        elements.tpContent.innerText = text;
        elements.tpContent.style.fontSize = `${state.teleprompter.fontSize}px`;
        elements.teleprompterModal.classList.remove('hidden');
        elements.teleprompterModal.classList.add('flex');
        document.body.style.overflow = 'hidden';
    }

    function closeTeleprompter() {
        stopTeleprompterScroll();
        elements.teleprompterModal.classList.add('hidden');
        elements.teleprompterModal.classList.remove('flex');
        document.body.style.overflow = '';
    }

    function startTeleprompterScroll() {
        state.teleprompter.isPlaying = true;
        elements.tpPlayPauseBtn.classList.replace('bg-indigo-600', 'bg-amber-600');
        elements.tpPlayPauseBtn.classList.replace('hover:bg-indigo-500', 'hover:bg-amber-500');
        elements.tpPlayPauseBtn.innerHTML = `<i class="fa-solid fa-pause"></i> <span>Pause</span>`;

        function scrollStep() {
            if (!state.teleprompter.isPlaying) return;
            const scrollSpeed = state.teleprompter.speed * 0.7;
            elements.tpViewport.scrollTop += scrollSpeed;

            if (elements.tpViewport.scrollTop + elements.tpViewport.clientHeight >= elements.tpViewport.scrollHeight - 50) {
                stopTeleprompterScroll();
                return;
            }
            state.teleprompter.animationFrameId = requestAnimationFrame(scrollStep);
        }

        state.teleprompter.animationFrameId = requestAnimationFrame(scrollStep);
    }

    function stopTeleprompterScroll() {
        state.teleprompter.isPlaying = false;
        if (state.teleprompter.animationFrameId) {
            cancelAnimationFrame(state.teleprompter.animationFrameId);
            state.teleprompter.animationFrameId = null;
        }
        elements.tpPlayPauseBtn.classList.replace('bg-amber-600', 'bg-indigo-600');
        elements.tpPlayPauseBtn.classList.replace('hover:bg-amber-500', 'hover:bg-indigo-500');
        elements.tpPlayPauseBtn.innerHTML = `<i class="fa-solid fa-play"></i> <span>Start</span>`;
    }

    function toggleTeleprompterPlay() {
        if (state.teleprompter.isPlaying) {
            stopTeleprompterScroll();
        } else {
            startTeleprompterScroll();
        }
    }

    function resetTeleprompter() {
        stopTeleprompterScroll();
        elements.tpViewport.scrollTop = 0;
    }

    // ==========================================
    // TOAST NOTIFICATION SYSTEM
    // ==========================================
    function showToast(message, type = 'success') {
        const toast = document.createElement('div');
        const icon = type === 'success' ? 'fa-circle-check text-emerald-400' : 'fa-circle-info text-indigo-400';
        toast.className = 'toast-in flex items-center gap-2.5 px-4 py-3 bg-slate-900 text-white rounded-xl shadow-xl border border-slate-800 text-xs font-medium max-w-sm';
        toast.innerHTML = `<i class="fa-solid ${icon}"></i> <span>${message}</span>`;
        
        elements.toastContainer.appendChild(toast);

        setTimeout(() => {
            toast.classList.replace('toast-in', 'toast-out');
            setTimeout(() => toast.remove(), 250);
        }, 2500);
    }

    // ==========================================
    // LOCAL STORAGE PERSISTENCE
    // ==========================================
    let autoSaveTimeout = null;
    function saveDraftToStorage() {
        if (autoSaveTimeout) clearTimeout(autoSaveTimeout);
        autoSaveTimeout = setTimeout(() => {
            localStorage.setItem('creatorkit_draft_text', elements.mainInput.value);
            elements.autoSaveBadge.style.opacity = '1';
            setTimeout(() => {
                elements.autoSaveBadge.style.opacity = '0.7';
            }, 1000);
        }, 400);
    }

    function loadDraftFromStorage() {
        const savedText = localStorage.getItem('creatorkit_draft_text');
        if (savedText !== null && savedText.trim() !== '') {
            elements.mainInput.value = savedText;
        } else {
            elements.mainInput.value = SAMPLE_DATA.social;
        }
        updateAnalytics(elements.mainInput.value);
        processActiveTool();
    }

    // ==========================================
    // THEME MANAGEMENT
    // ==========================================
    function initTheme() {
        const storedTheme = localStorage.getItem('creatorkit_theme') || 'dark';
        if (storedTheme === 'dark') {
            document.documentElement.classList.add('dark');
            elements.themeIcon.className = 'fa-solid fa-sun text-base text-amber-400';
        } else {
            document.documentElement.classList.remove('dark');
            elements.themeIcon.className = 'fa-solid fa-moon text-base text-slate-600';
        }
    }

    function toggleTheme() {
        const isDark = document.documentElement.classList.toggle('dark');
        if (isDark) {
            localStorage.setItem('creatorkit_theme', 'dark');
            elements.themeIcon.className = 'fa-solid fa-sun text-base text-amber-400';
            showToast('Dark mode activated');
        } else {
            localStorage.setItem('creatorkit_theme', 'light');
            elements.themeIcon.className = 'fa-solid fa-moon text-base text-slate-600';
            showToast('Light mode activated');
        }
    }

    // ==========================================
    // LEGAL MODALS (AdSense Compliance)
    // ==========================================
    const LEGAL_CONTENT = {
        about: {
            title: '<i class="fa-solid fa-circle-info text-indigo-500"></i> About CreatorKit Studio',
            html: `
                <p><strong>CreatorKit Studio</strong> is an open-access, browser-powered utility workspace crafted for YouTubers, Instagram and LinkedIn content creators, scriptwriters, copywriters, and SEO specialists.</p>
                <p class="mt-2">Our mission is to eliminate repetitive text formatting friction. Built with cutting-edge, 100% client-side JavaScript architecture, CreatorKit Studio guarantees that no scripts, captions, or intellectual property ever leave your device.</p>
                <h4 class="font-bold text-slate-800 dark:text-slate-200 mt-3 text-sm">Key Principles:</h4>
                <ul class="list-disc pl-5 space-y-1 mt-1">
                    <li><strong>Instant Execution:</strong> Zero server latency or API round-trips.</li>
                    <li><strong>Zero Tracking of Content:</strong> Keystrokes remain in local browser sandbox.</li>
                    <li><strong>Always Free:</strong> Maintained via transparent, non-intrusive Google AdSense advertising.</li>
                </ul>
            `
        },
        privacy: {
            title: '<i class="fa-solid fa-shield-halved text-indigo-500"></i> Privacy Policy',
            html: `
                <p><strong>Last Updated: 2026</strong></p>
                <p class="mt-2">Your privacy is fundamental to our architecture. This Privacy Policy details how CreatorKit Studio handles information:</p>
                <h4 class="font-bold text-slate-800 dark:text-slate-200 mt-3 text-sm">1. 100% Client-Side Processing</h4>
                <p>All text transformations (SRT subtitle cleaning, hashtag extraction, AI cliché sanitization, font conversion) are executed entirely inside your browser's JavaScript engine. We do not operate external processing servers or retain copies of your text.</p>
                <h4 class="font-bold text-slate-800 dark:text-slate-200 mt-3 text-sm">2. Local Storage</h4>
                <p>We utilize your browser's private <code>localStorage</code> API to remember your draft content and theme preference. This data never leaves your device.</p>
                <h4 class="font-bold text-slate-800 dark:text-slate-200 mt-3 text-sm">3. Google AdSense & Third-Party Cookies</h4>
                <p>We display third-party advertisements served by Google AdSense. Google uses cookies (including the DoubleClick cookie) to serve ads based on prior visits to this or other websites. You may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" class="text-indigo-500 underline">Google Ads Settings</a>.</p>
            `
        },
        terms: {
            title: '<i class="fa-solid fa-file-contract text-indigo-500"></i> Terms of Service',
            html: `
                <p><strong>1. Acceptance of Terms:</strong> By accessing and using CreatorKit Studio, you agree to comply with and be bound by these terms.</p>
                <p class="mt-2"><strong>2. Permitted Use:</strong> You may use all utilities for personal, educational, or commercial content creation workflows without fee.</p>
                <p class="mt-2"><strong>3. Disclaimer of Warranties:</strong> The utilities are provided "as is" without warranty of any kind. You are solely responsible for reviewing transformed text prior to publication.</p>
                <p class="mt-2"><strong>4. Intellectual Property:</strong> You retain 100% ownership and copyright of any content you input or generate with CreatorKit Studio.</p>
            `
        },
        contact: {
            title: '<i class="fa-solid fa-envelope text-indigo-500"></i> Contact Us',
            html: `
                <p>Have feature suggestions, bug reports, or partnership inquiries?</p>
                <p class="mt-2">Reach our development team directly at: <a href="mailto:support@creatorkitstudio.local" class="text-indigo-500 font-semibold underline">support@creatorkitstudio.local</a></p>
                <p class="mt-2 text-slate-400">We typically reply within 24–48 business hours.</p>
            `
        }
    };

    function openLegalModal(type) {
        const item = LEGAL_CONTENT[type];
        if (!item) return;
        elements.legalModalTitle.innerHTML = item.title;
        elements.legalModalBody.innerHTML = item.html;
        elements.legalModal.classList.remove('hidden');
        elements.legalModal.classList.add('flex');
    }

    function closeLegalModal() {
        elements.legalModal.classList.add('hidden');
        elements.legalModal.classList.remove('flex');
    }

    // ==========================================
    // SEARCH & FILTER UTILITIES
    // ==========================================
    function filterTools(query) {
        const q = query.toLowerCase().trim();
        const toolButtons = document.querySelectorAll('.tool-btn');
        let visibleCount = 0;

        toolButtons.forEach(btn => {
            const text = btn.innerText.toLowerCase();
            const keywords = (btn.dataset.keywords || '').toLowerCase();
            if (!q || text.includes(q) || keywords.includes(q)) {
                btn.style.display = 'flex';
                visibleCount++;
            } else {
                btn.style.display = 'none';
            }
        });

        document.querySelectorAll('.tool-category').forEach(cat => {
            const hasVisibleChild = Array.from(cat.querySelectorAll('.tool-btn')).some(b => b.style.display !== 'none');
            cat.style.display = hasVisibleChild ? 'block' : 'none';
        });

        elements.toolCountBadge.textContent = `${visibleCount} Tools`;
    }

    // Handle URL Hash Routes
    function handleHashRoute() {
        const hash = window.location.hash.replace('#', '').trim();
        if (hash) {
            const validTool = document.querySelector(`.tool-btn[data-action="${hash}"]`);
            if (validTool) {
                setActiveTool(hash, false);
                return;
            }
        }
        setActiveTool('fix-line-breaks', false);
    }

    // ==========================================
    // EVENT LISTENERS INITIALIZATION
    // ==========================================
    function initEventListeners() {
        elements.mainInput.addEventListener('input', () => {
            updateAnalytics(elements.mainInput.value);
            processActiveTool();
            saveDraftToStorage();
        });

        // Tool buttons clicks (Left Sidebar)
        document.querySelectorAll('.tool-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;
                setActiveTool(action);
                showToast(`Tool loaded: ${btn.innerText.trim()}`);
            });
        });

        // Quick action bar buttons (Center panel)
        document.querySelectorAll('.action-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;
                setActiveTool(action);
            });
        });

        // Copy to clipboard
        elements.copyOutputBtn.addEventListener('click', async () => {
            const textToCopy = elements.mainOutput.value;
            if (!textToCopy) {
                showToast('Nothing to copy yet!', 'info');
                return;
            }

            try {
                if (navigator.clipboard && window.isSecureContext) {
                    await navigator.clipboard.writeText(textToCopy);
                } else {
                    elements.mainOutput.select();
                    document.execCommand('copy');
                }
                
                elements.copyFeedbackBadge.classList.remove('hidden');
                setTimeout(() => elements.copyFeedbackBadge.classList.add('hidden'), 1500);

                showToast('Copied transformed text to clipboard!');
            } catch (err) {
                showToast('Failed to copy. Please select and copy manually.', 'info');
            }
        });

        // Send Output back to Input
        elements.sendToInputBtn.addEventListener('click', () => {
            const outputText = elements.mainOutput.value;
            if (!outputText) {
                showToast('No output to send!', 'info');
                return;
            }
            elements.mainInput.value = outputText;
            updateAnalytics(outputText);
            saveDraftToStorage();
            processActiveTool();
            showToast('Output transferred to input!');
        });

        // Download output file (.txt)
        elements.downloadOutputBtn.addEventListener('click', () => {
            const content = elements.mainOutput.value;
            if (!content) {
                showToast('No content to download!', 'info');
                return;
            }
            const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `creatorkit-${state.activeTool}-${Date.now()}.txt`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            showToast('File downloaded successfully!');
        });

        // Paste from clipboard
        elements.pasteBtn.addEventListener('click', async () => {
            try {
                if (navigator.clipboard) {
                    const text = await navigator.clipboard.readText();
                    elements.mainInput.value = text;
                    updateAnalytics(text);
                    processActiveTool();
                    saveDraftToStorage();
                    showToast('Pasted from clipboard!');
                } else {
                    showToast('Please paste using Ctrl+V / Cmd+V', 'info');
                }
            } catch (err) {
                showToast('Clipboard access denied. Please use Ctrl+V', 'info');
            }
        });

        // Clear input button
        elements.clearInputBtn.addEventListener('click', () => {
            elements.mainInput.value = '';
            elements.mainOutput.value = '';
            updateAnalytics('');
            saveDraftToStorage();
            showToast('Input cleared');
        });

        // Clear all / Reset button
        elements.clearAllBtn.addEventListener('click', () => {
            if (confirm('Reset workspace and clear current draft?')) {
                elements.mainInput.value = '';
                elements.mainOutput.value = '';
                localStorage.removeItem('creatorkit_draft_text');
                updateAnalytics('');
                showToast('Workspace reset to blank');
            }
        });

        // Theme Toggle
        elements.themeToggleBtn.addEventListener('click', toggleTheme);

        // Search inputs
        elements.sidebarToolSearch.addEventListener('input', (e) => filterTools(e.target.value));
        elements.headerToolSearch.addEventListener('input', (e) => {
            elements.sidebarToolSearch.value = e.target.value;
            filterTools(e.target.value);
        });

        // Hash change router
        window.addEventListener('hashchange', handleHashRoute);

        // Keyboard Shortcut Ctrl+K & Esc
        window.addEventListener('keydown', (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
                e.preventDefault();
                elements.headerToolSearch.focus();
            }
            if (e.key === 'Escape') {
                closeTeleprompter();
                closeLegalModal();
            }
            if (e.code === 'Space' && !elements.teleprompterModal.classList.contains('hidden')) {
                e.preventDefault();
                toggleTeleprompterPlay();
            }
        });

        // Preset Sample Loaders
        elements.sampleSrtBtn.addEventListener('click', () => {
            elements.mainInput.value = SAMPLE_DATA.srt;
            setActiveTool('clean-srt');
            updateAnalytics(SAMPLE_DATA.srt);
            saveDraftToStorage();
            showToast('Loaded SRT Subtitle sample');
        });

        elements.sampleAiBtn.addEventListener('click', () => {
            elements.mainInput.value = SAMPLE_DATA.ai;
            setActiveTool('clean-ai-artifacts');
            updateAnalytics(SAMPLE_DATA.ai);
            saveDraftToStorage();
            showToast('Loaded AI Draft sample');
        });

        elements.sampleSocialBtn.addEventListener('click', () => {
            elements.mainInput.value = SAMPLE_DATA.social;
            setActiveTool('fix-line-breaks');
            updateAnalytics(SAMPLE_DATA.social);
            saveDraftToStorage();
            showToast('Loaded Social Post sample');
        });

        elements.sampleScriptBtn.addEventListener('click', () => {
            elements.mainInput.value = SAMPLE_DATA.script;
            setActiveTool('speech-timer');
            updateAnalytics(SAMPLE_DATA.script);
            saveDraftToStorage();
            showToast('Loaded Video Script sample');
        });

        // Teleprompter Controls
        elements.teleprompterLaunchBtn.addEventListener('click', openTeleprompter);
        elements.tpCloseBtn.addEventListener('click', closeTeleprompter);
        elements.tpPlayPauseBtn.addEventListener('click', toggleTeleprompterPlay);
        elements.tpResetBtn.addEventListener('click', resetTeleprompter);

        elements.tpSpeedSlider.addEventListener('input', (e) => {
            state.teleprompter.speed = parseInt(e.target.value, 10);
            elements.tpSpeedValue.textContent = state.teleprompter.speed;
        });

        elements.tpFontSlider.addEventListener('input', (e) => {
            state.teleprompter.fontSize = parseInt(e.target.value, 10);
            elements.tpFontValue.textContent = `${state.teleprompter.fontSize}px`;
            elements.tpContent.style.fontSize = `${state.teleprompter.fontSize}px`;
        });

        elements.tpMirrorBtn.addEventListener('click', () => {
            state.teleprompter.isMirrored = !state.teleprompter.isMirrored;
            if (state.teleprompter.isMirrored) {
                elements.tpContent.classList.add('prompter-mirrored');
                elements.tpMirrorBtn.classList.replace('bg-slate-800', 'bg-indigo-600');
                showToast('Teleprompter mirror mode enabled');
            } else {
                elements.tpContent.classList.remove('prompter-mirrored');
                elements.tpMirrorBtn.classList.replace('bg-indigo-600', 'bg-slate-800');
                showToast('Teleprompter standard mode');
            }
        });

        // Legal Modals Listeners
        elements.openAboutBtn.addEventListener('click', () => openLegalModal('about'));
        elements.openPrivacyBtn.addEventListener('click', () => openLegalModal('privacy'));
        elements.openTermsBtn.addEventListener('click', () => openLegalModal('terms'));
        elements.openContactBtn.addEventListener('click', () => openLegalModal('contact'));
        elements.closeLegalModalBtn.addEventListener('click', closeLegalModal);
        elements.closeLegalModalFooterBtn.addEventListener('click', closeLegalModal);

        elements.legalModal.addEventListener('click', (e) => {
            if (e.target === elements.legalModal) closeLegalModal();
        });
    }

    // ==========================================
    // APP INITIALIZATION
    // ==========================================
    function init() {
        initTheme();
        initEventListeners();
        loadDraftFromStorage();
        handleHashRoute();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
