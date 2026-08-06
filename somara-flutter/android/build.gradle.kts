allprojects {
    repositories {
        // Repositório local com os artefactos do motor do Flutter.
        //
        // Vem primeiro de propósito: nesta rede o cliente TLS do Java não
        // consegue sequer fazer um HEAD a storage.googleapis.com ("server
        // may not support TLSv1.2/1.3"), mesmo com o ficheiro já em cache —
        // o Gradle revalida por rede e falha. O curl descarrega o mesmo
        // ficheiro sem problema, por isso guardamo-lo aqui e o Gradle
        // resolve-o do disco, sem tocar na rede.
        //
        // Os ficheiros ficam fora do git (ver .gitignore); num ambiente com
        // rede saudável esta pasta simplesmente não existe e o Gradle usa o
        // repositório oficial do Flutter como sempre.
        maven { url = uri("${rootProject.projectDir}/flutter-engine-repo") }
        google()
        mavenCentral()
    }
}

val newBuildDir: Directory =
    rootProject.layout.buildDirectory
        .dir("../../build")
        .get()
rootProject.layout.buildDirectory.value(newBuildDir)

subprojects {
    val newSubprojectBuildDir: Directory = newBuildDir.dir(project.name)
    project.layout.buildDirectory.value(newSubprojectBuildDir)
}
subprojects {
    project.evaluationDependsOn(":app")
}

tasks.register<Delete>("clean") {
    delete(rootProject.layout.buildDirectory)
}
