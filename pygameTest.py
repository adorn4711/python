# Importieren der Pygame-Bibliothek
import pygame

# initialisieren von pygame
pygame.init()
# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

# Titel für Fensterkopf
pygame.display.set_caption("Unser erstes Pygame-Spiel")
# Fenster öffnen
screen = pygame.display.set_mode((640, 480))

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while spielaktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrueckt")

            # Taste für Spieler 1
            if event.key == pygame.K_RIGHT:
                print("Spieler hat Pfeiltaste rechts gedrueckt")
            elif event.key == pygame.K_LEFT:
                print("Spieler hat Pfeiltaste links gedrueckt")
            elif event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste hoch gedrueckt")
            elif event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrueckt")
            elif event.key == pygame.K_SPACE:
                print("Spieler hat Leertaste gedrueckt")

            # Taste für Spieler 2
            elif event.key == pygame.K_w:
                print("Spieler hat Taste w gedrueckt")
            elif event.key == pygame.K_a:
                print("Spieler hat Taste a gedrueckt")
            elif event.key == pygame.K_s:
                print("Spieler hat Taste s gedrueckt")
            elif event.key == pygame.K_d:
                print("Spieler hat Taste d gedrueckt")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hast Maus angeklickt")

# Spiellogik hier integrieren

    # Spielfeld löschen
    screen.fill(WEISS)

    # Spielfeld/figuren zeichnen
    pygame.draw.rect(screen, ROT, [10, 20, 100, 100], 1)

    # normale Linie (orange)
    pygame.draw.line(screen, ORANGE, [10, 20], [100, 120])

    # Linie mit Antialiasing (rot)
    pygame.draw.aaline(screen, ROT, [20, 20], [110, 120])

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)
# End Schleife Hauptprogramm
print("End of game")
pygame.quit()
