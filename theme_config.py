# theme_config.py

THEMES = {
    # ------------------------------------------------------------------
    # STYLE 1: NEON TECH
    # ------------------------------------------------------------------
    "neon_tech": {
        "name": "Neon Data",
        "colors": {
            "bg": "#050505",
            "text_main": "#E5E5E5",
            "text_accent": "#CCFF00", 
            "shape": "#1A1A1A",
            "secondary": "#333333",
        },
        "fonts": {
            "title_size": 95,
            "body_size": 48,
            "meta_size": 30,
            "number_size": 140
        },
        "layout": {
            "margin_left": 120,
            "header_y": 40,
            "title_y_start": 250,
            "body_y_start": 600,
            "number_pos": (830, 1150)
        },
        "graphics": {
            "blur_strength": 3,
            "grid_size": 80,          
            "top_bar_height": 120,    
            "accent_line_y": 120,     
            "bar_width": 40,          
            "bar_gap": 20,
            "bar_max_height": 200     
        }
    },

    # ------------------------------------------------------------------
    # STYLE 2: SWISS GRID
    # ------------------------------------------------------------------
    "swiss_red": {
        "name": "Swiss Grid",
        "colors": {
            "bg": "#F4F4F0",
            "text_main": "#111111",
            "text_accent": "#FF3B30",
            "shape": "#CCCCCC",
            "secondary": "#999999",
        },
        "fonts": {
            "title_size": 95,
            "body_size": 48,
            "meta_size": 30,
            "number_size": 140
        },
        "layout": {
            "margin_left": 120,
            "header_y": 60,
            "title_y_start": 250,
            "body_y_start": 600,
            "number_pos": (830, 20)
        },
        "graphics": {
            "blur_strength": 4,
            "top_line_y": 150,
            "bottom_line_y": 1150,
            "side_bar_width": 5,      
            "shape_size": 200,        
            "shape_x": 800,           
            "shape_y": 900            
        }
    },

    # ------------------------------------------------------------------
    # STYLE 3: OBSIDIAN GLOW
    # ------------------------------------------------------------------
    "obsidian_glow": {
        "name": "Obsidian",
        "colors": {
            "bg": "#0F1115",
            "text_main": "#FFFFFF",
            "text_accent": "#7C3AED", 
            "shape": "#1E293B",
            "secondary": "#38BDF8",   
        },
        "fonts": {
            "title_size": 95,
            "body_size": 48,
            "meta_size": 30,
            "number_size": 140
        },
        "layout": {
            "margin_left": 100,       
            "header_y": 50,
            "title_y_start": 250,
            "body_y_start": 600,
            "number_pos": (830, 1150)
        },
        "graphics": {
            "blur_strength": 8,
            "ellipse_offset": 40,     
            "card_width": 80,         
            "card_height": 120,
            "card_gap": 30,
            "card_base_y": 1100       
        }
    },

    # ------------------------------------------------------------------
    # STYLE 4: DEEP OCEAN
    # ------------------------------------------------------------------
    "deep_ocean": {
        "name": "Deep Ocean",
        "colors": {
            "bg": "#0f172a",
            "text_main": "#f8fafc",
            "text_accent": "#38bdf8", 
            "shape": "#1e293b",
            "secondary": "#0ea5e9",
        },
        "fonts": {
            "title_size": 95,
            "body_size": 48,
            "meta_size": 30,
            "number_size": 140
        },
        "layout": {
            "margin_left": 120,
            "header_y": 50,
            "title_y_start": 250,
            "body_y_start": 600,
            "number_pos": (830, 1150)
        },
        "graphics": {
            "blur_strength": 2,
            "line_spacing": 40,      
            "highlight_every": 3     
        }
    },

    # ------------------------------------------------------------------
    # STYLE 5: GOLDEN LUXE
    # ------------------------------------------------------------------
    "golden_luxe": {
        "name": "Golden Luxe",
        "colors": {
            "bg": "#1c1917",
            "text_main": "#e7e5e4",
            "text_accent": "#f59e0b", 
            "shape": "#292524",
            "secondary": "#78350f",
        },
        "fonts": {
            "title_size": 95,
            "body_size": 48,
            "meta_size": 30,
            "number_size": 140
        },
        "layout": {
            "margin_left": 120,
            "header_y": 50,
            "title_y_start": 250,
            "body_y_start": 600,
            "number_pos": (830, 1150)
        },
        "graphics": {
            "blur_strength": 4,
            "border_margin": 50,     
            "border_width": 2
        }
    },

    # ------------------------------------------------------------------
    # STYLE 6: MINIMAL GREY (NEW)
    # ------------------------------------------------------------------
    "minimal_grey": {
        "name": "Minimal Grey",
        "colors": {
            "bg": "#F3F4F6",        # Light grayish white
            "text_main": "#111827", # Very dark charcoal
            "text_accent": "#6B7280", # Medium cool gray
            "shape": "#E5E7EB",     # Light gray for shapes
            "secondary": "#D1D5DB", # Lighter gray
        },
        "fonts": {
            "title_size": 95,
            "body_size": 48,
            "meta_size": 30,
            "number_size": 140
        },
        "layout": {
            "margin_left": 120,
            "header_y": 50,
            "title_y_start": 250,
            "body_y_start": 600,
            "number_pos": (830, 1150)
        },
        "graphics": {
            "blur_strength": 6,       # Soft blur for the circles
            "circle_size": 500,       # Large soft circles
            "line_y": 1050            # Subtle divider line
        }
    }
}