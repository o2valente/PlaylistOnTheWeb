<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="root">

        <ul id="myTable" class="breadcrumb">
            <xsl:for-each select="artista">
                <li>
                    <img style="width: 120px; height: 120px;">
                        <xsl:attribute name="src">
                            <xsl:value-of select="imagem"/>
                        </xsl:attribute>
                    </img>
                    <xsl:variable name="id" select="id"/>
                    <a href="http://127.0.0.1:8000/artistTracks?id={$id}">
                        <xsl:value-of select="name"/>
                    </a>
                </li>
            </xsl:for-each>
        </ul>

    </xsl:template>
</xsl:stylesheet>