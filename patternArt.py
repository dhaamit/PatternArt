import turtle
import random


def drawPattern(x, clr):
    # Create a turtle object
    t = turtle.Turtle()
    t.speed(0)
    y=x/2
    # Write the text
    t.penup()
    t.goto(-730, 430)
    t.pendown()
    t.write(clr[3], font=("Arial", 16, "normal"), align="left")
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for j in range(60):
        for i in range(4):
            t.color(clr[0])
            if x < 80:
                t.forward(y)
            else:
                break
            t.left(x)
        for k in range(4):
            t.color(clr[1])
            if x < 80:
                t.backward(j + y + 3)
            else:
                break
            t.right(x-45)
        for l in range(4):
            t.color(clr[2])
            if l + x - 10 < 80:
                t.forward(j+ l + y - 10)
            else:
                break
            t.right(x - 20)
    t.clear()
    t.hideturtle()
    pass


screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
color_palettes= [["#8C5E58", "#C4A484", "#F3E9DC", "Earth Tones"],
                  ["#5D9CEC", "#4A90E2", "#34495E", "Cool Blues"],
                  ["#F7CAC9", "#DEC4E8", "#F3E5AB", "soft Pastels"],
                  ["#1B4D3E", "#3D8361", "#88B04B", "Forest Greens"],
                  ["#F44336", "#4CAF50", "#2196F3", "Bold Contras"],
                  ["#FF6F61", "#FFB400", "#FFDB4D", "sunset Vibes"],
                  ["#B0A8B9", "#D5C6E0", "#F8F1F1", "Muted Neutrals"],
                  ["#6C5B7B", "#C06C84", "#F8B195", "Vintage Hues"],
                  ["#FF5722", "#FFC107", "#FFEB3B", "Energetic Burs"],
                  ["#05668D", "#028090", "#00A896", "Ocean Calm"],
                  ["#283149", "#404B69", "#DBEDF3", "Cool Grays"],
                  ["#2E4053", "#2471A3", "#1ABC9C", "Deep Blues"],
                  ["#FF9A8B", "#FF6A88", "#FF99AC", "Pink Gradient"],
                  ["#D7263D", "#FF5700", "#FF8A5C", "Warm Reds"],
                  ["#E63946", "#F1FAEE", "#457B9D", "Rustic Elegance"],
                  ["#264653", "#2A9D8F", "#E9C46A", "Desert Greens"],
                  ["#F4A261", "#E76F51", "#2A1A1F", "Autumn Vibes"],
                  ["#6D6875", "#B5838D", "#FFCAD4", "Dusty Romance"],
                  ["#90A955", "#31572C", "#FFE156", "Vibrant Greens"],
                  ["#003049", "#D62828", "#F77F00", "Modern Reds"],
                  ["#E63946", "#6A0572", "#4A4E69", "Regal shades"],
                  ["#F3722C", "#F8961E", "#F9C74F", "Citrus Burst"],
                  ["#370617", "#6A0572", "#A4133C", "Dramatic Reds"],
                  ["#2C2C54", "#706FD3", "#F7D794", "Midnight Blues"],
                  ["#FBE7C6", "#FFD56B", "#6A0572", "Cheerful Yellow"],
                  ["#06D6A0", "#118AB2", "#073B4C", "Teal Power"],
                  ["#EF476F", "#FFD166", "#118AB2", "summer Pop"],
                  ["#14213D", "#FCA311", "#E5E5E5", "Industrial Chic"],
                  ["#E63946", "#9A031E", "#5F0A87", "Electric Reds"],
                  ["#52B788", "#40916C", "#1B4332", "Mossy Greens"],
                  ["#F72585", "#7209B7", "#3A0CA3", "Electric Purples"],
                  ["#005F73", "#0A9396", "#94D2BD", "Ocean Greens"],
                  ["#FFB4A2", "#E5989B", "#B5838D", "Soft Pinks"],
                  ["#D8F3DC", "#95D5B2", "#52B788", "Mint Greens"],
                  ["#EA698B", "#D55D92", "#C05299", "Berry Tones"],
                  ["#001219", "#005F73", "#94D2BD", "Deep Ocean"],
                  ["#6A0572", "#AB83A1", "#DABAD2", "Elegant Mauves"],
                  ["#0A9396", "#94D2BD", "#E9D8A6", "Coastal Calm"],
                  ["#A4133C", "#D00000", "#FFBA08", "Bold Reds"],
                  ["#0077B6", "#00B4D8", "#90E0EF", "Light Blues"],
                  ["#FFBA08", "#FAA307", "#F48C06", "Warm Oranges"],
                  ["#5F0A87", "#8E44AD", "#BE95C4", "Royal Purples"],
                  ["#393E46", "#00ADB5", "#EEEEEE", "Modern Monochrome"],
                  ["#B5838D", "#FFB4A2", "#6A0572", "Soft Reds"],
                  ["#2D6A4F", "#40916C", "#74C69D", "Earthy Greens"],
                  ["#5A189A", "#9A031E", "#FF9F1C", "Vibrant Contrast"],
                  ["#2B2D42", "#8D99AE", "#EDF2F4", "Minimal Grays"],
                  ["#D7263D", "#3A0CA3", "#4361EE", "High-Energy Blues"],
                  ["#E63946", "#F1FAEE", "#A8DADC", "Calm Waters"],
                  ["#7E5234", "#C68B59", "#F1C27D", "Rustic Browns"]
                  ]
for a in range(100):
    randomNumber = random.randint(0, 49)
    drawPattern(randomNumber, color_palettes[randomNumber])

# Keep the window open until manually closed
turtle.done()
