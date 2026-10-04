plugins {
    id("com.android.application")
    // The Flutter Gradle Plugin must be applied after the Android and Kotlin Gradle plugins.
    id("dev.flutter.flutter-gradle-plugin")
}

android {
    namespace = "mz.co.takova.somara"
    compileSdk = flutter.compileSdkVersion
    // Sem ndkVersion de propósito: a app não tem código C/C++ nenhum, e o
    // motor do Flutter já vem compilado. Declarar o NDK obrigaria a
    // descarregar ~1 GB de toolchain que nunca chegaria a ser usada.

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    // A versão de testes, pedida com `-Pteste=true`.
    //
    // Dá-lhe outro identificador de aplicação e outro nome debaixo do
    // ícone, e é isso que permite ter as duas no mesmo telemóvel ao mesmo
    // tempo, cada uma com os seus dados. Sem o sufixo, instalar a de testes
    // apagava a normal — e o progresso das duas misturava-se.
    //
    // Não são `productFlavors` de propósito: uma propriedade do Gradle faz
    // o mesmo em seis linhas, sem pastas de código novas nem mais variantes
    // para o Gradle montar.
    val teste = project.hasProperty("teste")

    defaultConfig {
        // TODO: Specify your own unique Application ID (https://developer.android.com/studio/build/application-id.html).
        applicationId = "mz.co.takova.somara"
        // You can update the following values to match your application needs.
        // For more information, see: https://flutter.dev/to/review-gradle-config.
        minSdk = flutter.minSdkVersion
        targetSdk = flutter.targetSdkVersion
        versionCode = flutter.versionCode
        versionName = flutter.versionName

        if (teste) {
            applicationIdSuffix = ".teste"
        }
        // O nome debaixo do ícone entra por substituição no manifesto, que
        // lá tem `android:label="${appName}"`.
        //
        // Não é um `resValue`: a partir do AGP 9 os valores de recurso
        // gerados vêm desligados por omissão, e ligá-los era acender uma
        // funcionalidade inteira do Gradle para escrever uma palavra.
        manifestPlaceholders["appName"] = if (teste) "Somara TESTE" else "Somara"
    }

    buildTypes {
        release {
            // TODO: Add your own signing config for the release build.
            // Signing with the debug keys for now, so `flutter run --release` works.
            signingConfig = signingConfigs.getByName("debug")
        }
    }
}

kotlin {
    compilerOptions {
        jvmTarget = org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_17
    }
}

flutter {
    source = "../.."
}
