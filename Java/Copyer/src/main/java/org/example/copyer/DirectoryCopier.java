package org.example.copyer;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

public class DirectoryCopier {

    private String suffix = "decrypted";

    public String getSuffix() {
        return suffix;
    }

    public void setSuffix(String suffix) {
        this.suffix = suffix;
    }

    public void copyFolder(File source, File target) throws IOException {
        Path sourceDirectory = source.toPath();
        Path targetDirectory = sourceDirectory.resolveSibling(sourceDirectory.getFileName() + "_" + DateUtil.format("MM-dd HH-mm-ss"));

        try {
            // 确保目标目录不存在
            if (!Files.exists(targetDirectory)) {
                // 创建目标目录
                Files.createDirectories(targetDirectory);
                // 遍历源目录
                Files.walk(sourceDirectory).forEach(sourcePath -> {
                    try {
                        // 计算目标路径
                        Path targetPath = targetDirectory.resolve(sourceDirectory.relativize(sourcePath));
                        // 根据源路径类型（目录还是文件）来创建或复制
                        if (Files.isDirectory(sourcePath)) {
                            if (!Files.exists(targetPath)) {
                                Files.createDirectory(targetPath);
                            }
                        } else {
                            Files.copy(sourcePath, targetPath, StandardCopyOption.REPLACE_EXISTING);
                        }
                    } catch (IOException e) {
                        e.fillInStackTrace();
                    }
                });
            }
        } catch (IOException e) {
            e.fillInStackTrace();
        }
    }

    public String getFileExtension(File file) {
        String fileName = file.getName();
        int lastIndex = fileName.lastIndexOf('.');

        if (lastIndex == -1 || lastIndex == 0) {
            return "";
        } else {
            return fileName.substring(lastIndex + 1);
        }
    }

    public String getFilename(File file) {
        String fileName = file.getName();
        int lastIndex = fileName.lastIndexOf('.');

        if (lastIndex > 0) {
            return fileName.substring(0, lastIndex);
        } else {
            return fileName;
        }
    }

    public void copyFile(File file, byte[] data) throws IOException {
        String filepath = file.getParent();
        String filename = getFilename(file);
        filepath = filepath + "\\" + filename + "_" + DateUtil.format("MM-dd HH-mm-ss") + "." + getFileExtension(file);
        try (FileOutputStream outputStream = new FileOutputStream(filepath)) {
            outputStream.write(data);
        }
    }

}
