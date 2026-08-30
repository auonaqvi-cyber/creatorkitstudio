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
        activeWorkspace: 'all', // 'all' | 'blogger' | 'creator'
        fancyStyle: 'bold-sans',
        caseFormat: 'title',
        teleprompter: {
            isPlaying: false,
            speed: 3,
            fontSize: 44,
            isMirrored: false,
            animationFrameId: null
        },
        imageResizer: {
            currentImage: null,
            originalWidth: 0,
            originalHeight: 0,
            aspectRatio: 1,
            lockedAspect: true,
            mimeType: 'image/png'
        }
    };

    // DOM Elements Cache
    const elements = {
        // Metadata & Schema
        pageTitle: document.getElementById('pageTitle'),
        pageMetaDescription: document.getElementById('pageMetaDescription'),
        ogTitle: document.getElementById('ogTitle'),
        ogDescription: document.getElementById('ogDescription'),
        faqSchema: document.getElementById('faqSchema'),
        dynamicSeoGuide: document.getElementById('dynamicSeoGuide'),

        // Cards & Viewports
        standardWorkspaceCard: document.getElementById('standardWorkspaceCard'),
        imageResizerCard: document.getElementById('imageResizerCard'),
        analyticsBarContainer: document.getElementById('analyticsBarContainer'),
        dynamicCustomWidget: document.getElementById('dynamicCustomWidget'),

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

        // Search, Workspace Mode & Filters
        headerToolSearch: document.getElementById('headerToolSearch'),
        sidebarToolSearch: document.getElementById('sidebarToolSearch'),
        toolsListContainer: document.getElementById('toolsListContainer'),
        toolCountBadge: document.getElementById('toolCountBadge'),
        workspaceTabBtns: document.querySelectorAll('.workspace-tab-btn'),

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

        // Image Resizer Elements
        imgDropzone: document.getElementById('imgDropzone'),
        imgFileInput: document.getElementById('imgFileInput'),
        imgControls: document.getElementById('imgControls'),
        imgWidthInput: document.getElementById('imgWidthInput'),
        imgHeightInput: document.getElementById('imgHeightInput'),
        imgAspectLock: document.getElementById('imgAspectLock'),
        imgFormatSelect: document.getElementById('imgFormatSelect'),
        downloadResizedImgBtn: document.getElementById('downloadResizedImgBtn'),
        resizerCanvas: document.getElementById('resizerCanvas'),

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
            chars: '𝘢𝘣𝘤𝘥𝘦𝗳𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘃𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡0123456789',
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

    // Sample Datasets
    const SAMPLE_DATA = {
        srt: `1\n00:00:01,200 --> 00:00:04,500\nWelcome back to CreatorKit Studio!\n\n2\n00:00:04,800 --> 00:00:08,150\nToday we are showing you how to clean <b>SRT subtitles</b> instantly.\n\n3\n00:00:08,400 --> 00:00:12,900\nNo more manual timestamp deletion or broken line breaks in your video scripts!`,
        ai: `**In today's fast-paced digital world**, creating high-converting content is more important than ever. \n\nIn this article, we delve into the tapestry of modern social algorithms — unlocking growth for creators.\n\n**Key Takeaways:**\n* Point 1: Always format clean captions.\n* Point 2: Avoid cliché AI phrases like "In conclusion" or "delve into".\n\nIn conclusion, having client-side creator tools elevates your workflow!`,
        social: `Stop struggling with cramped Instagram and LinkedIn captions! \n\nWhen you post multiple paragraphs on social media, the mobile app often squishes everything together.\n\nWith CreatorKit Studio:\n1. Write your draft with clean double spacing.\n2. Hit "Fix Paragraphs".\n3. Paste directly to Instagram, Threads, or LinkedIn.\n\n#contentcreator #marketing #socialmediatips #copywriting #growthhacks #creatorlife`,
        script: `Have you ever wondered why top creators post every single day without burning out? \n\nThe secret isn't working 14 hours a day. It's having an automated system for writing, cleaning, and pacing your voiceovers.\n\nAt a standard conversational pace of 130 words per minute, this 65-word script takes precisely 30 seconds to record for a viral TikTok or YouTube Short. Clean, punchy, and straight to the point!`
    };

    // ==========================================
    // CORE UTILITY ALGORITHMS
    // ==========================================

    // 1. Line Break & Paragraph Fixer
    function fixLineBreaks(text) {
        if (!text) return '';
        const lines = text.split(/\r?\n/);
        return lines.map(line => line.trim() === '' ? '\u200B' : line).join('\n');
    }

    // 2. Hashtag Generator (Multi-Platform Categorized)
    function generateHashtags(input) {
        if (!input || !input.trim()) return '';
        const cleaned = input.toLowerCase().replace(/[^a-z0-9\s]/g, '').trim();
        const words = cleaned.split(/\s+/).filter(w => w.length > 2);
        const mainKeyword = words.join('');
        const primaryTag = words[0] || 'creator';

        const platformSets = {
            instagram: [
                `#${mainKeyword}`, `#${primaryTag}`, `#${primaryTag}tips`, `#${primaryTag}life`,
                `#${primaryTag}hacks`, `#contentcreator`, `#socialmediatips`, `#creators`,
                `#digitalcreator`, `#viralpost`, `#instatips`, `#growthhacks`
            ],
            tiktok: [
                `#${mainKeyword}`, `#${primaryTag}tok`, `#${primaryTag}tutorial`, `#learnontiktok`,
                `#fyp`, `#foryoupage`, `#viral`, `#trending`, `#xyzbca`
            ],
            shorts: [
                `#${mainKeyword}`, `#shorts`, `#youtubeshorts`, `#${primaryTag}`, `#ytshorts`,
                `#viralshorts`, `#shortsfeed`, `#creator`
            ],
            linkedin: [
                `#${primaryTag}`, `#${primaryTag}strategy`, `#marketing`, `#growth`,
                `#productivity`, `#leadership`, `#contentstrategy`
            ]
        };

        return `📱 INSTAGRAM HASHTAG SET:\n${platformSets.instagram.join(' ')}\n\n` +
               `🎵 TIKTOK SEARCH HASHTAG SET:\n${platformSets.tiktok.join(' ')}\n\n` +
               `▶️ YOUTUBE SHORTS TAG SET:\n${platformSets.shorts.join(' ')}\n\n` +
               `💼 LINKEDIN PROFESSIONAL SET:\n${platformSets.linkedin.join(' ')}`;
    }

    // 3. Twitter / X Thread Splitter
    function splitIntoTwitterThread(text) {
        if (!text || !text.trim()) return [];
        const sentences = text.match(/[^.!?\n]+[.!?\n]+/g) || [text];
        const maxLen = 270;
        const tweets = [];
        let currentTweet = '';

        sentences.forEach(sentence => {
            const trimmed = sentence.trim();
            if (!trimmed) return;

            if ((currentTweet + ' ' + trimmed).trim().length <= maxLen) {
                currentTweet = (currentTweet + ' ' + trimmed).trim();
            } else {
                if (currentTweet) tweets.push(currentTweet);
                currentTweet = trimmed;
            }
        });
        if (currentTweet) tweets.push(currentTweet);

        const total = tweets.length;
        return tweets.map((tw, i) => `(${i + 1}/${total}) ${tw}`);
    }

    // 4. Flesch-Kincaid Readability Analyzer Math
    function countSyllablesInWord(word) {
        let clean = word.toLowerCase().replace(/[^a-z]/g, '');
        if (clean.length <= 3) return 1;
        clean = clean.replace(/(?:[^laeiouy]es|ed|[^laeiouy]e)$/, '');
        clean = clean.replace(/^y/, '');
        const matches = clean.match(/[aeiouy]{1,2}/g);
        return matches ? matches.length : 1;
    }

    function calculateReadability(text) {
        if (!text || !text.trim()) {
            return { words: 0, sentences: 0, syllables: 0, readingEase: 0, gradeLevel: 0, label: 'No text', tips: 'Paste text to analyze.' };
        }

        const wordsArray = text.trim().match(/[\w\u00C0-\u024F\u0400-\u04FF'-]+/g) || [];
        const words = wordsArray.length || 1;
        const sentencesArray = text.trim().match(/[^.!?]+[.!?]+(\s|$)/g) || [text];
        const sentences = sentencesArray.length || 1;

        let totalSyllables = 0;
        let complexWords = 0;
        wordsArray.forEach(w => {
            const syl = countSyllablesInWord(w);
            totalSyllables += syl;
            if (syl >= 3) complexWords++;
        });

        // Flesch Reading Ease Formula
        let ease = 206.835 - (1.015 * (words / sentences)) - (84.6 * (totalSyllables / words));
        ease = Math.max(0, Math.min(100, Math.round(ease)));

        // Flesch-Kincaid Grade Level Formula
        let grade = (0.39 * (words / sentences)) + (11.8 * (totalSyllables / words)) - 15.59;
        grade = Math.max(1, Math.round(grade * 10) / 10);

        let label = 'Standard (Conversational)';
        let badgeColor = 'text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950/60';
        let tips = 'Optimal conversational score. Effortless to read on mobile devices.';

        if (ease >= 80) {
            label = 'Very Easy (5th–6th Grade)';
            badgeColor = 'text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/60';
            tips = 'Simple, fast-paced readability. Great for high-converting social copy.';
        } else if (ease >= 60) {
            label = 'Standard (8th Grade Sweet Spot)';
            badgeColor = 'text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950/60';
            tips = 'Industry gold standard for blog posts, YouTube scripts, and newsletters.';
        } else if (ease >= 40) {
            label = 'Fairly Difficult (High School / College)';
            badgeColor = 'text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/60';
            tips = 'Slightly dense. Shorten long sentences and reduce 3-syllable words.';
        } else {
            label = 'Very Difficult (Academic / Legal)';
            badgeColor = 'text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/60';
            tips = 'High cognitive load. Split compound sentences and eliminate technical jargon.';
        }

        return {
            words,
            sentences,
            syllables: totalSyllables,
            complexWordsPercent: Math.round((complexWords / words) * 100),
            avgWordsPerSentence: (words / sentences).toFixed(1),
            readingEase: ease,
            gradeLevel: grade,
            label,
            badgeColor,
            tips
        };
    }

    // 5. SEO Title & Meta Description Generator
    function generateSEOMeta(text) {
        if (!text || !text.trim()) {
            return {
                title: 'CreatorKit Studio | Free Creator Utility Suite',
                description: 'Boost your content workflow with fast client-side utilities. Zero server latency and 100% privacy.',
                raw: ''
            };
        }

        const lines = text.split(/\r?\n/).map(l => l.trim()).filter(Boolean);
        let firstLine = lines[0] || 'Content Creator Tools & Guide';
        
        let title = firstLine.replace(/^[#\*\-_\s]+/, '').replace(/[\*\_\`]/g, '');
        if (title.length > 55) {
            title = title.substring(0, 52) + '...';
        }
        if (title.length < 35) {
            title += ' | Complete Guide & Tips';
        }

        const fullContent = lines.join(' ').replace(/[\*\_\`\#]/g, '');
        let desc = fullContent.substring(0, 155).trim();
        if (fullContent.length > 155) {
            desc += '...';
        }

        const raw = `<!-- SEO Meta Tags for <head> -->\n` +
                    `<title>${title}</title>\n` +
                    `<meta name="description" content="${desc}">\n\n` +
                    `<!-- Open Graph / Social Sharing -->\n` +
                    `<meta property="og:title" content="${title}">\n` +
                    `<meta property="og:description" content="${desc}">`;

        return { title, description: desc, raw };
    }

    // 6. Fancy Unicode Text Generator
    function generateFancyText(text, style = 'bold-sans') {
        if (!text) return '';
        const fontMap = UNICODE_FONTS[style] || UNICODE_FONTS['bold-sans'];
        const fontChars = Array.from(fontMap.chars);
        const plainChars = Array.from(PLAIN_ALPHABET);

        let result = '';
        for (const char of text) {
            const index = plainChars.indexOf(char);
            result += (index !== -1 && fontChars[index]) ? fontChars[index] : char;
        }
        return result;
    }

    // 7. Hashtag Extractor & Cleaner
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
        return uniqueTags.slice(0, maxCount).join(' ');
    }

    // 8. Case Converter
    function convertCase(text, format = 'title') {
        if (!text) return '';
        switch (format) {
            case 'upper': return text.toUpperCase();
            case 'lower': return text.toLowerCase();
            case 'sentence': return text.toLowerCase().replace(/(^\s*\w|[.!?]\s+\w)/g, c => c.toUpperCase());
            case 'capitalize': return text.replace(/\b\w/g, c => c.toUpperCase());
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
            default: return text;
        }
    }

    // 9. SRT Caption Cleaner
    function cleanSRT(srtContent) {
        if (!srtContent) return '';
        let cleaned = srtContent
            .replace(/^WEBVTT[^\n]*\n+/i, '')
            .replace(/\d{1,2}:\d{2}:\d{2}[,\.]\d{3}\s*-->\s*\d{1,2}:\d{2}:\d{2}[,\.]\d{3}[^\n]*/g, '')
            .replace(/^\s*\d+\s*$/gm, '')
            .replace(/<\/?[^>]+(>|$)/g, '')
            .replace(/\{[^\}]+\}/g, '');

        return cleaned.split(/\r?\n/).map(l => l.trim()).filter(Boolean).join('\n\n');
    }

    // 10. Script Speaking Duration Calculator
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

    // 11. AI Formatting & Cliché Cleaner
    function cleanAIArtifacts(text) {
        if (!text) return '';
        let cleaned = text
            .replace(/\*\*(.*?)\*\*/g, '$1')
            .replace(/\*(.*?)\*/g, '$1')
            .replace(/__(.*?)__/g, '$1')
            .replace(/`([^`]+)`/g, '$1')
            .replace(/^#{1,6}\s+/gm, '')
            .replace(/^[-\*]\s+/gm, '• ')
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

        for (const regex of cliches) cleaned = cleaned.replace(regex, '');
        return cleaned.trim();
    }

    // 12. SEO Slug Generator
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

    // 13. Whitespace Trimmer
    function cleanWhitespace(text) {
        if (!text) return '';
        return text.split(/\r?\n/).map(l => l.replace(/[ \t]+/g, ' ').trim()).filter((l, i, a) => !(l === '' && a[i - 1] === '')).join('\n').trim();
    }

    // 14. Duplicate Line Filter
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
        const readingDisplay = readingMin > 0 ? `${readingMin}m ${readingSec % 60}s` : `${readingSec}s`;

        const speakingSec = Math.round((words / 130) * 60);
        const speakingMin = Math.floor(speakingSec / 60);
        const speakingDisplay = speakingMin > 0 ? `${speakingMin}m ${speakingSec % 60}s` : `${speakingSec}s`;

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
    // WORKSPACE MODE & TAB SWITCHER (All / Blogger / Creator)
    // ==========================================
    function filterWorkspace(mode, save = true) {
        state.activeWorkspace = mode;
        if (save) {
            localStorage.setItem('activeWorkspace', mode);
            localStorage.setItem('creatorkit_active_workspace', mode);
        }

        const tabButtons = document.querySelectorAll('[data-tab], .tab-btn');
        const toolItems = document.querySelectorAll('.tool-card[data-category], .tool-btn[data-category]');
        const categoryBlocks = document.querySelectorAll('.space-y-1, .category-group');

        // 1. Update active tab UI styling
        tabButtons.forEach(btn => {
            const btnMode = (btn.getAttribute('data-tab') || btn.innerText).toLowerCase();
            if (btnMode.includes(mode)) {
                btn.classList.add('bg-indigo-600', 'text-white', 'active');
                btn.classList.remove('text-slate-400');
            } else {
                btn.classList.remove('bg-indigo-600', 'text-white', 'active');
                btn.classList.add('text-slate-400');
            }
        });

        // 2. Hide/Show individual tools
        let visibleCount = 0;
        const searchQuery = (elements.sidebarToolSearch ? elements.sidebarToolSearch.value : '').toLowerCase().trim();

        toolItems.forEach(item => {
            const category = item.getAttribute('data-category') || '';
            const text = item.innerText.toLowerCase();
            const keywords = (item.dataset.keywords || '').toLowerCase();

            const matchesSearch = !searchQuery || text.includes(searchQuery) || keywords.includes(searchQuery);
            const matchesMode = mode === 'all' || category.includes(mode);

            if (matchesMode && matchesSearch) {
                item.style.display = '';
                visibleCount++;
            } else {
                item.style.display = 'none';
            }
        });

        // 3. Hide empty category headers if no visible tools remain under them
        categoryBlocks.forEach(block => {
            const visibleChildren = block.querySelectorAll('[data-category]:not([style*="display: none"])');
            const header = block.previousElementSibling; // Category title header

            if (mode !== 'all' && visibleChildren.length === 0) {
                block.style.display = 'none';
                if (header && (header.classList.contains('text-xs') || header.classList.contains('category-header'))) {
                    header.style.display = 'none';
                }
            } else {
                block.style.display = '';
                if (header && (header.classList.contains('text-xs') || header.classList.contains('category-header'))) {
                    header.style.display = '';
                }
            }
        });

        const modeLabel = mode === 'all' ? 'All' : (mode === 'blogger' ? 'Blogger' : 'Creator');
        if (elements.toolCountBadge) {
            elements.toolCountBadge.textContent = `${visibleCount} in ${modeLabel}`;
        }
    }

    const setWorkspaceMode = filterWorkspace;

    // Expose globally for inline event handler fallbacks
    window.switchWorkspaceTab = filterWorkspace;
    window.filterWorkspace = filterWorkspace;
    window.setActiveTool = setActiveTool;

    // ==========================================
    // DYNAMIC SEO GUIDE & SCHEMA.ORG RENDERER
    // ==========================================
    function renderSeoGuide(toolId) {
        if (typeof SEO_GUIDES === 'undefined') return;
        const guide = SEO_GUIDES[toolId] || SEO_GUIDES['fix-line-breaks'];
        if (!guide) return;

        if (elements.pageTitle) elements.pageTitle.textContent = guide.title;
        if (elements.pageMetaDescription) elements.pageMetaDescription.setAttribute('content', guide.metaDescription);
        if (elements.ogTitle) elements.ogTitle.setAttribute('content', guide.title);
        if (elements.ogDescription) elements.ogDescription.setAttribute('content', guide.metaDescription);

        if (elements.faqSchema && guide.faqs) {
            const schemaData = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": guide.faqs.map(faq => ({
                    "@type": "Question",
                    "name": faq.q,
                    "acceptedAnswer": { "@type": "Answer", "text": faq.a }
                }))
            };
            elements.faqSchema.textContent = JSON.stringify(schemaData, null, 2);
        }

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
                <p class="mt-3 text-xs text-slate-600 dark:text-slate-400 leading-relaxed">${faq.a}</p>
            </details>
        `).join('');

        elements.dynamicSeoGuide.innerHTML = `
            <div class="space-y-6">
                <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-200 dark:border-dark-border pb-3">
                    <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 border border-indigo-200/60 dark:border-indigo-800/40">
                        <i class="fa-solid fa-book-open"></i> ${guide.badge || 'Creator Educational Guide'}
                    </span>
                    <div class="flex flex-wrap gap-1.5">${keywordsPills}</div>
                </div>

                <!-- Structured Tool Usage Card (150-250 words semantic instructions) -->
                ${guide.quickGuide || ''}

                <h2 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">${guide.h2}</h2>
                <div class="guide-body">${guide.contentHtml}</div>

                <div class="pt-6 border-t border-slate-200 dark:border-dark-border space-y-3">
                    <h3 class="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2 mb-3">
                        <i class="fa-solid fa-circle-question text-indigo-500"></i> Frequently Asked Questions & Best Practices
                    </h3>
                    <div class="space-y-2.5">${faqsHtml}</div>
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

        elements.dynamicCustomWidget.classList.add('hidden');
        elements.dynamicCustomWidget.innerHTML = '';

        switch (state.activeTool) {
            case 'fix-line-breaks':
                outputText = fixLineBreaks(inputText);
                break;
            case 'hashtag-generator':
                outputText = generateHashtags(inputText);
                break;
            case 'thread-splitter': {
                const threadChunks = splitIntoTwitterThread(inputText);
                outputText = threadChunks.join('\n\n---\n\n');
                
                if (threadChunks.length > 0) {
                    elements.dynamicCustomWidget.classList.remove('hidden');
                    const cardsHtml = threadChunks.map((tweet, idx) => `
                        <div class="p-3.5 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl space-y-2 relative">
                            <div class="flex items-center justify-between text-[11px]">
                                <span class="font-bold text-cyan-600 dark:text-cyan-400 font-mono">Tweet ${idx + 1} of ${threadChunks.length}</span>
                                <span class="text-slate-400 font-mono">${tweet.length}/280 chars</span>
                            </div>
                            <p class="text-xs text-slate-800 dark:text-slate-200 whitespace-pre-wrap">${tweet}</p>
                            <button type="button" class="copy-tweet-btn px-2.5 py-1 rounded bg-slate-200 dark:bg-slate-800 hover:bg-cyan-600 hover:text-white text-[11px] font-semibold text-slate-700 dark:text-slate-300 transition flex items-center gap-1">
                                <i class="fa-regular fa-copy"></i> Copy Tweet ${idx + 1}
                            </button>
                        </div>
                    `).join('');

                    elements.dynamicCustomWidget.innerHTML = `
                        <div class="space-y-2">
                            <span class="text-[11px] font-bold uppercase text-slate-400 block"><i class="fa-brands fa-x-twitter text-cyan-500 mr-1"></i> Interactive Thread Deck (${threadChunks.length} Tweets):</span>
                            <div class="space-y-2.5">${cardsHtml}</div>
                        </div>
                    `;

                    elements.dynamicCustomWidget.querySelectorAll('.copy-tweet-btn').forEach((btn, idx) => {
                        btn.addEventListener('click', async () => {
                            await navigator.clipboard.writeText(threadChunks[idx]);
                            showToast(`Copied Tweet ${idx + 1} to clipboard!`);
                        });
                    });
                }
                break;
            }
            case 'readability-score': {
                const readData = calculateReadability(inputText);
                outputText = `📊 FLESCH-KINCAID READABILITY BREAKDOWN:\n` +
                    `--------------------------------------\n` +
                    `• Flesch Reading Ease: ${readData.readingEase} / 100 (${readData.label})\n` +
                    `• Flesch-Kincaid Grade Level: Grade ${readData.gradeLevel}\n` +
                    `• Average Words per Sentence: ${readData.avgWordsPerSentence} words\n` +
                    `• Complex Multi-Syllable Words: ${readData.complexWordsPercent}%\n` +
                    `• Total Sentences: ${readData.sentences} | Total Words: ${readData.words}\n\n` +
                    `Editorial Recommendation:\n` +
                    `--------------------------------------\n` +
                    `${readData.tips}`;

                elements.dynamicCustomWidget.classList.remove('hidden');
                elements.dynamicCustomWidget.innerHTML = `
                    <div class="p-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl space-y-3">
                        <div class="flex flex-wrap items-center justify-between gap-2">
                            <span class="text-xs font-bold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                                <i class="fa-solid fa-glasses text-emerald-500"></i> Readability Grade Assessment
                            </span>
                            <span class="text-xs font-extrabold px-2.5 py-1 rounded-full ${readData.badgeColor}">${readData.label}</span>
                        </div>
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                            <div class="p-2 bg-white dark:bg-slate-800 rounded-lg border border-slate-100 dark:border-slate-700">
                                <span class="text-[10px] text-slate-400 block">Reading Ease</span>
                                <span class="text-lg font-bold font-mono text-indigo-600 dark:text-indigo-400">${readData.readingEase} / 100</span>
                            </div>
                            <div class="p-2 bg-white dark:bg-slate-800 rounded-lg border border-slate-100 dark:border-slate-700">
                                <span class="text-[10px] text-slate-400 block">Grade Level</span>
                                <span class="text-lg font-bold font-mono text-emerald-600 dark:text-emerald-400">Grade ${readData.gradeLevel}</span>
                            </div>
                            <div class="p-2 bg-white dark:bg-slate-800 rounded-lg border border-slate-100 dark:border-slate-700">
                                <span class="text-[10px] text-slate-400 block">Avg Words/Sentence</span>
                                <span class="text-base font-bold font-mono text-slate-700 dark:text-slate-200">${readData.avgWordsPerSentence}</span>
                            </div>
                            <div class="p-2 bg-white dark:bg-slate-800 rounded-lg border border-slate-100 dark:border-slate-700">
                                <span class="text-[10px] text-slate-400 block">Complex Words</span>
                                <span class="text-base font-bold font-mono text-slate-700 dark:text-slate-200">${readData.complexWordsPercent}%</span>
                            </div>
                        </div>
                        <p class="text-xs text-slate-600 dark:text-slate-400 italic bg-white dark:bg-slate-800 p-2.5 rounded-lg border border-slate-100 dark:border-slate-700">
                            💡 <strong>Tip:</strong> ${readData.tips}
                        </p>
                    </div>
                `;
                break;
            }
            case 'seo-meta-generator': {
                const seo = generateSEOMeta(inputText);
                outputText = seo.raw;

                elements.dynamicCustomWidget.classList.remove('hidden');
                elements.dynamicCustomWidget.innerHTML = `
                    <div class="p-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-dark-border rounded-xl space-y-2 shadow-sm">
                        <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-1 flex items-center gap-1.5">
                            <i class="fa-brands fa-google text-indigo-500"></i> Google SERP Live Snippet Preview:
                        </span>
                        <div class="p-3 bg-white dark:bg-slate-950 rounded-lg border border-slate-200 dark:border-slate-800 font-sans space-y-1">
                            <div class="flex items-center gap-2 text-xs text-slate-500">
                                <span class="w-4 h-4 rounded-full bg-indigo-600 text-white text-[9px] flex items-center justify-center font-bold">C</span>
                                <span class="text-slate-700 dark:text-slate-300 text-[11px]">creatorkitstudio.pro &rsaquo; blog</span>
                            </div>
                            <h3 class="text-sm font-semibold text-blue-600 dark:text-blue-400 hover:underline cursor-pointer leading-snug">${seo.title}</h3>
                            <p class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">${seo.description}</p>
                        </div>
                        <div class="flex items-center justify-between text-[11px] text-slate-400 pt-1">
                            <span>Title Length: <strong class="font-mono text-slate-700 dark:text-slate-200">${seo.title.length}/60 chars</strong></span>
                            <span>Meta Length: <strong class="font-mono text-slate-700 dark:text-slate-200">${seo.description.length}/160 chars</strong></span>
                        </div>
                    </div>
                `;
                break;
            }
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
            case 'image-resizer':
                outputText = 'Image Resizer Active. Use the Canvas dropzone above to scale your photo locally.';
                break;
            default:
                outputText = inputText;
        }

        elements.mainOutput.value = outputText;

        if (outputText && outputText !== inputText && state.activeTool !== 'image-resizer') {
            elements.outputChangeBadge.classList.remove('hidden');
            elements.outputChangeBadge.textContent = 'Transformed ✓';
        } else {
            elements.outputChangeBadge.classList.add('hidden');
        }
    }

    // Dynamic Sub-options Toolbar
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
            elements.dynamicToolOptions.querySelectorAll('#fancyStyleOptions button').forEach(btn => {
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
            elements.dynamicToolOptions.querySelectorAll('#caseFormatOptions button').forEach(btn => {
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

    // Set Active Tool
    function setActiveTool(toolAction, updateHash = true) {
        state.activeTool = toolAction;

        if (updateHash && window.location.hash !== `#${toolAction}`) {
            history.pushState(null, '', `#${toolAction}`);
        }

        // Toggle standard card vs image resizer card
        if (toolAction === 'image-resizer') {
            elements.imageResizerCard.classList.remove('hidden');
            elements.standardWorkspaceCard.classList.add('hidden');
        } else {
            elements.imageResizerCard.classList.add('hidden');
            elements.standardWorkspaceCard.classList.remove('hidden');
        }

        // Update sidebar buttons
        document.querySelectorAll('.tool-btn').forEach(btn => {
            if (btn.dataset.action === toolAction) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // Update quick action bar buttons
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

        if (window.innerWidth < 768) {
            const drawer = document.getElementById('mobileToolDrawer');
            if (drawer && drawer.hasAttribute('open')) {
                drawer.removeAttribute('open');
            }
        }
    }

    // ==========================================
    // CLIENT-SIDE IMAGE RESIZER & CANVAS ENGINE
    // ==========================================
    function initImageResizer() {
        const dropzone = elements.imgDropzone;
        const fileInput = elements.imgFileInput;

        dropzone.addEventListener('click', () => fileInput.click());

        dropzone.addEventListener('dragover', (e) => {
            e.preventDefault();
            dropzone.classList.add('border-indigo-500', 'bg-indigo-50/20');
        });

        dropzone.addEventListener('dragleave', () => {
            dropzone.classList.remove('border-indigo-500', 'bg-indigo-50/20');
        });

        dropzone.addEventListener('drop', (e) => {
            e.preventDefault();
            dropzone.classList.remove('border-indigo-500', 'bg-indigo-50/20');
            if (e.dataTransfer.files && e.dataTransfer.files[0]) {
                loadImageFile(e.dataTransfer.files[0]);
            }
        });

        fileInput.addEventListener('change', (e) => {
            if (e.target.files && e.target.files[0]) {
                loadImageFile(e.target.files[0]);
            }
        });

        elements.imgAspectLock.addEventListener('change', (e) => {
            state.imageResizer.lockedAspect = e.target.checked;
        });

        elements.imgWidthInput.addEventListener('input', () => {
            const w = parseInt(elements.imgWidthInput.value, 10);
            if (w > 0 && state.imageResizer.lockedAspect && state.imageResizer.aspectRatio) {
                const h = Math.round(w / state.imageResizer.aspectRatio);
                elements.imgHeightInput.value = h;
            }
            renderCanvasPreview();
        });

        elements.imgHeightInput.addEventListener('input', () => {
            const h = parseInt(elements.imgHeightInput.value, 10);
            if (h > 0 && state.imageResizer.lockedAspect && state.imageResizer.aspectRatio) {
                const w = Math.round(h * state.imageResizer.aspectRatio);
                elements.imgWidthInput.value = w;
            }
            renderCanvasPreview();
        });

        document.querySelectorAll('.preset-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const w = parseInt(btn.dataset.w, 10);
                const h = parseInt(btn.dataset.h, 10);
                elements.imgWidthInput.value = w;
                elements.imgHeightInput.value = h;
                renderCanvasPreview();
                showToast(`Preset loaded: ${w}×${h}`);
            });
        });

        elements.imgFormatSelect.addEventListener('change', (e) => {
            state.imageResizer.mimeType = e.target.value;
        });

        elements.downloadResizedImgBtn.addEventListener('click', () => {
            if (!state.imageResizer.currentImage) {
                showToast('Please upload an image first!', 'info');
                return;
            }

            const canvas = elements.resizerCanvas;
            const mime = state.imageResizer.mimeType || 'image/png';
            const ext = mime.split('/')[1] === 'jpeg' ? 'jpg' : mime.split('/')[1];

            canvas.toBlob((blob) => {
                if (!blob) return;
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `creatorkit-resized-${canvas.width}x${canvas.height}.${ext}`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
                showToast(`Image scaled to ${canvas.width}×${canvas.height} downloaded!`);
            }, mime, 0.92);
        });
    }

    function loadImageFile(file) {
        if (!file.type.startsWith('image/')) {
            showToast('Please select a valid image file (PNG, JPG, WebP)', 'info');
            return;
        }

        const reader = new FileReader();
        reader.onload = (e) => {
            const img = new Image();
            img.onload = () => {
                state.imageResizer.currentImage = img;
                state.imageResizer.originalWidth = img.width;
                state.imageResizer.originalHeight = img.height;
                state.imageResizer.aspectRatio = img.width / img.height;

                elements.imgWidthInput.value = img.width;
                elements.imgHeightInput.value = img.height;
                elements.imgControls.classList.remove('hidden');

                renderCanvasPreview();
                showToast(`Loaded ${file.name} (${img.width}×${img.height}px)`);
            };
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }

    function renderCanvasPreview() {
        if (!state.imageResizer.currentImage) return;
        const w = parseInt(elements.imgWidthInput.value, 10) || 100;
        const h = parseInt(elements.imgHeightInput.value, 10) || 100;

        const canvas = elements.resizerCanvas;
        canvas.width = w;
        canvas.height = h;

        const ctx = canvas.getContext('2d');
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = 'high';
        ctx.drawImage(state.imageResizer.currentImage, 0, 0, w, h);
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
        if (state.teleprompter.isPlaying) stopTeleprompterScroll();
        else startTeleprompterScroll();
    }

    function resetTeleprompter() {
        stopTeleprompterScroll();
        elements.tpViewport.scrollTop = 0;
    }

    // ==========================================
    // TOAST NOTIFICATIONS & PERSISTENCE
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

    let autoSaveTimeout = null;
    function saveDraftToStorage() {
        if (autoSaveTimeout) clearTimeout(autoSaveTimeout);
        autoSaveTimeout = setTimeout(() => {
            localStorage.setItem('creatorkit_draft_text', elements.mainInput.value);
            elements.autoSaveBadge.style.opacity = '1';
            setTimeout(() => elements.autoSaveBadge.style.opacity = '0.7', 1000);
        }, 400);
    }

    function loadDraftFromStorage() {
        const savedText = localStorage.getItem('creatorkit_draft_text');
        elements.mainInput.value = (savedText !== null && savedText.trim() !== '') ? savedText : SAMPLE_DATA.social;
        updateAnalytics(elements.mainInput.value);
        processActiveTool();
    }

    // ==========================================
    // THEME & LEGAL MODALS
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

    const LEGAL_CONTENT = {
        about: {
            title: '<i class="fa-solid fa-circle-info text-indigo-500"></i> About CreatorKit Studio',
            html: `<p><strong>CreatorKit Studio</strong> is an open-access, browser-powered utility workspace crafted for YouTubers, Instagram and LinkedIn content creators, scriptwriters, copywriters, and SEO specialists.</p><p class="mt-2">Built with 100% client-side JavaScript architecture, CreatorKit Studio guarantees zero server uploads and zero data retention.</p>`
        },
        privacy: {
            title: '<i class="fa-solid fa-shield-halved text-indigo-500"></i> Privacy Policy',
            html: `<p><strong>100% Client-Side Privacy:</strong> All text and image operations run locally inside your browser sandbox. We do not store or transmit your content to external servers.</p><p class="mt-2">We display third-party advertisements served by Google AdSense.</p>`
        },
        terms: {
            title: '<i class="fa-solid fa-file-contract text-indigo-500"></i> Terms of Service',
            html: `<p>You retain 100% ownership and copyright of any content you input or generate with CreatorKit Studio.</p>`
        },
        contact: {
            title: '<i class="fa-solid fa-envelope text-indigo-500"></i> Contact Us',
            html: `<p>Reach our team at: <a href="mailto:support@creatorkitstudio.pro" class="text-indigo-500 font-semibold underline">support@creatorkitstudio.pro</a></p>`
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

    function filterTools(query = '') {
        const q = (query || '').toLowerCase().trim();
        const mode = state.activeWorkspace;
        const toolButtons = document.querySelectorAll('.tool-btn');
        let visibleCount = 0;

        toolButtons.forEach(btn => {
            const text = btn.innerText.toLowerCase();
            const keywords = (btn.dataset.keywords || '').toLowerCase();
            const modes = (btn.dataset.modes || 'all').split(',');

            const matchesSearch = !q || text.includes(q) || keywords.includes(q);
            const matchesMode = mode === 'all' || modes.includes(mode);

            if (matchesSearch && matchesMode) {
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

        const modeLabel = mode === 'all' ? 'All' : (mode === 'blogger' ? 'Blogger' : 'Creator');
        elements.toolCountBadge.textContent = `${visibleCount} in ${modeLabel}`;
    }

    function handleHashRoute() {
        const hash = window.location.hash.replace('#', '').trim();
        
        if (hash === 'all' || hash === 'blogger' || hash === 'creator') {
            setWorkspaceMode(hash, true);
            return;
        }

        if (hash) {
            const validToolBtn = document.querySelector(`.tool-btn[data-action="${hash}"]`);
            if (validToolBtn) {
                const modes = (validToolBtn.dataset.modes || 'all').split(',');
                if (state.activeWorkspace !== 'all' && !modes.includes(state.activeWorkspace)) {
                    setWorkspaceMode('all', false);
                }
                setActiveTool(hash, false);
                return;
            }
        }
        
        // Default initial tool
        setActiveTool('fix-line-breaks', false);
    }

    // ==========================================
    // INITIALIZATION & LISTENERS
    // ==========================================
    function initEventListeners() {
        elements.mainInput.addEventListener('input', () => {
            updateAnalytics(elements.mainInput.value);
            processActiveTool();
            saveDraftToStorage();
        });

        document.querySelectorAll('.tool-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                setActiveTool(btn.dataset.action);
                showToast(`Tool loaded: ${btn.innerText.trim()}`);
            });
        });

        document.querySelectorAll('.action-btn').forEach(btn => {
            btn.addEventListener('click', () => setActiveTool(btn.dataset.action));
        });

        // 3-Way Workspace Tabs Click Handlers
        const tabButtons = document.querySelectorAll('[data-tab], .tab-btn');
        tabButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const text = (btn.getAttribute('data-tab') || btn.innerText).toLowerCase();
                let mode = 'all';
                if (text.includes('blogger')) mode = 'blogger';
                else if (text.includes('creator')) mode = 'creator';
                
                filterWorkspace(mode, true);
                const title = mode === 'all' ? 'All Tools' : (mode === 'blogger' ? 'Blogger Mode' : 'Creator Mode');
                showToast(`Switched to ${title}`);
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
                showToast('Copied result to clipboard!');
            } catch (err) {
                showToast('Failed to copy. Please copy manually.', 'info');
            }
        });

        // Send Output back to Input
        elements.sendToInputBtn.addEventListener('click', () => {
            const outputText = elements.mainOutput.value;
            if (!outputText) return showToast('No output to send!', 'info');
            elements.mainInput.value = outputText;
            updateAnalytics(outputText);
            saveDraftToStorage();
            processActiveTool();
            showToast('Output transferred to input!');
        });

        // Download Output as text
        elements.downloadOutputBtn.addEventListener('click', () => {
            const content = elements.mainOutput.value;
            if (!content) return showToast('No content to download!', 'info');
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

        // Paste & Clear
        elements.pasteBtn.addEventListener('click', async () => {
            try {
                if (navigator.clipboard) {
                    const text = await navigator.clipboard.readText();
                    elements.mainInput.value = text;
                    updateAnalytics(text);
                    processActiveTool();
                    saveDraftToStorage();
                    showToast('Pasted from clipboard!');
                }
            } catch (err) {
                showToast('Please paste using Ctrl+V', 'info');
            }
        });

        elements.clearInputBtn.addEventListener('click', () => {
            elements.mainInput.value = '';
            elements.mainOutput.value = '';
            updateAnalytics('');
            saveDraftToStorage();
            showToast('Input cleared');
        });

        elements.clearAllBtn.addEventListener('click', () => {
            if (confirm('Reset workspace and clear current draft?')) {
                elements.mainInput.value = '';
                elements.mainOutput.value = '';
                localStorage.removeItem('creatorkit_draft_text');
                updateAnalytics('');
                showToast('Workspace reset');
            }
        });

        // Theme Toggle & Search
        elements.themeToggleBtn.addEventListener('click', toggleTheme);
        elements.sidebarToolSearch.addEventListener('input', (e) => filterTools(e.target.value));
        elements.headerToolSearch.addEventListener('input', (e) => {
            elements.sidebarToolSearch.value = e.target.value;
            filterTools(e.target.value);
        });

        window.addEventListener('hashchange', handleHashRoute);

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
            showToast('Loaded SRT Subtitles');
        });

        elements.sampleAiBtn.addEventListener('click', () => {
            elements.mainInput.value = SAMPLE_DATA.ai;
            setActiveTool('clean-ai-artifacts');
            updateAnalytics(SAMPLE_DATA.ai);
            saveDraftToStorage();
            showToast('Loaded AI Draft');
        });

        elements.sampleSocialBtn.addEventListener('click', () => {
            elements.mainInput.value = SAMPLE_DATA.social;
            setActiveTool('fix-line-breaks');
            updateAnalytics(SAMPLE_DATA.social);
            saveDraftToStorage();
            showToast('Loaded Social Post');
        });

        elements.sampleScriptBtn.addEventListener('click', () => {
            elements.mainInput.value = SAMPLE_DATA.script;
            setActiveTool('speech-timer');
            updateAnalytics(SAMPLE_DATA.script);
            saveDraftToStorage();
            showToast('Loaded Video Script');
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

        // Initialize Image Resizer
        initImageResizer();
    }

    function init() {
        initTheme();
        initEventListeners();

        // Restore saved workspace mode
        const savedMode = localStorage.getItem('activeWorkspace') || localStorage.getItem('creatorkit_active_workspace') || 'all';
        setWorkspaceMode(savedMode, false);

        loadDraftFromStorage();
        handleHashRoute();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
