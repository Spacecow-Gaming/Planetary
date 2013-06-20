JFLAGS = -g
JC = javac
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $*.java

CLASSES = \
	MainClass.java \
	mainMenu.java \
	explore.java \
	game.java \
	mine.java \
	sector.java \
	shop.java \
	build.java

default: classes

classes: $(CLASSES:.java=.class)

jar: classes
	jar cvfm0 Planetary.jar manifest.txt $(CLASSES:.java=.class)
clean: $(classes) $(jar)
	$(RM) *.class
