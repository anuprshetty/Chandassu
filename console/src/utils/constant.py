class Constant:
    kannada_unicode_range = {"start": 3202, "end": 3299}
    kannada_symbols = {
        "alphabets": [
            "ಾ",
            "ಿ",
            "ೀ",
            "ು",
            "ೂ",
            "ೃ",
            "ೄ",
            "ೆ",
            "ೇ",
            "ೈ",
            "ೊ",
            "ೋ",
            "ೌ",
            "ಂ",
            "ಃ",
        ],
        "halant": "್",
        "halant_letters": [
            "ಕ್",
            "ಖ್",
            "ಗ್",
            "ಘ್",
            "ಙ್",
            "ಚ್",
            "ಛ್",
            "ಜ್",
            "ಝ್",
            "ಞ್",
            "ಟ್",
            "ಠ್",
            "ಡ್",
            "ಢ್",
            "ಣ್",
            "ತ್",
            "ಥ್",
            "ದ್",
            "ಧ್",
            "ನ್",
            "ಪ್",
            "ಫ್",
            "ಬ್",
            "ಭ್",
            "ಮ್",
            "ಯ್",
            "ರ್",
            "ಲ್",
            "ವ್",
            "ಶ್",
            "ಷ್",
            "ಸ್",
            "ಹ್",
            "ಳ್",
        ],
        "guru_letters": [
            "ಆ",
            "ಈ",
            "ಊ",
            "ೠ",
            "ಏ",
            "ಐ",
            "ಓ",
            "ಔ",
            "ಾ",
            "ೀ",
            "ೂ",
            "ೄ",
            "ೇ",
            "ೈ",
            "ೋ",
            "ೌ",
            "ಂ",
            "ಃ",
        ],
    }

    prastara_info = {
        "space": {"symbol": " ", "value": 0},
        "laghu": {"symbol": "U", "value": 1},
        "guru": {"symbol": "_ ", "value": 2},
    }
    gana_symbol = "|"

    chandassu_names = {
        "chandassu": "ಛಂದಸ್ಸು",
        "kandapadya": "ಕಂದ ಪದ್ಯ",
        "shatpadi": {
            "shatpadi": "ಷಟ್ಪದಿ",
            "shara": "ಶರ ಷಟ್ಪದಿ",
            "kusuma": "ಕುಸುಮ ಷಟ್ಪದಿ",
            "bhoga": "ಭೋಗ ಷಟ್ಪದಿ",
            "bhamini": "ಭಾಮಿನೀ ಷಟ್ಪದಿ",
            "vardhaka": "ವಾರ್ಧಕ ಷಟ್ಪದಿ",
            "parivardhini": "ಪರಿವರ್ಧಿನೀ ಷಟ್ಪದಿ",
        },
        "ragale": {
            "ragale": "ರಗಳೆ",
            "utsaha": "ಉತ್ಸಾಹ ರಗಳೆ",
            "mandanila": "ಮಂದಾನಿಲ ರಗಳೆ",
            "lalita": "ಲಲಿತ ರಗಳೆ",
        },
        "vrutta": {
            "vrutta": "ಖ್ಯಾತಕರ್ಣಾಟಕ ವೃತ್ತಗಳು",
            "utpala_mala": "ಉತ್ಪಲಮಾಲಾ ವೃತ್ತ",
            "champaka_mala": "ಚಂಪಕಮಾಲಾ ವೃತ್ತ",
            "shardula_vikreedita": "ಶಾರ್ದೂಲವಿಕ್ರೀಡಿತ ವೃತ್ತ",
            "mattebha_vikreedita": "ಮತ್ತೇಭವಿಕ್ರೀಡಿತ ವೃತ್ತ",
            "sragdhara": "ಸ್ರಗ್ಧರಾ ವೃತ್ತ",
            "maha_sragdhara": "ಮಹಾಸ್ರಗ್ಧರಾ ವೃತ್ತ",
        },
        "invalid": "ಈ ಪದ್ಯವು ಯಾವ ಛಂದಸ್ಸಿಗೂ ಸೇರಿಲ್ಲ.",
    }

    chandassu_kannada_names = [
        "ಇತರೆ",
        "ಕಂದ ಪದ್ಯ",
        "ಶರ ಷಟ್ಪದಿ",
        "ಕುಸುಮ ಷಟ್ಪದಿ",
        "ಭೋಗ ಷಟ್ಪದಿ",
        "ಭಾಮಿನೀ ಷಟ್ಪದಿ",
        "ವಾರ್ಧಕ ಷಟ್ಪದಿ",
        "ಪರಿವರ್ಧಿನೀ ಷಟ್ಪದಿ",
        "ಉತ್ಸಾಹ ರಗಳೆ",
        "ಮಂದಾನಿಲ ರಗಳೆ",
        "ಲಲಿತ ರಗಳೆ",
        "ಉತ್ಪಲಮಾಲಾ ವೃತ್ತ",
        "ಚಂಪಕಮಾಲಾ ವೃತ್ತ",
        "ಶಾರ್ದೂಲವಿಕ್ರೀಡಿತ ವೃತ್ತ",
        "ಮತ್ತೇಭವಿಕ್ರೀಡಿತ ವೃತ್ತ",
        "ಸ್ರಗ್ಧರಾ ವೃತ್ತ",
        "ಮಹಾಸ್ರಗ್ಧರಾ ವೃತ್ತ",
    ]
