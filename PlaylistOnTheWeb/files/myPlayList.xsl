<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="root">
            <table id="breadcrumb_album"  class="breadcrumb">
                <thead></thead>
                <tbody id="data-table">
                <xsl:for-each select="playlistDemo">
                    <xsl:variable name="ID" select="position()"/>
                    <tr style="height: 130px; border-bottom:2px solid white;">
                        <td style="width: 200px;">
                            <strong><u><i>NAME:</i></u></strong> <xsl:text>  </xsl:text>
                            <xsl:value-of select="nome"/> <br />
                            <strong><u><i>ID:</i></u></strong> <xsl:text>  </xsl:text>
                            <xsl:value-of select="id"/>  <br />
                            <strong><u><i>TRACKS:</i></u></strong> <xsl:text>  </xsl:text>
                            <xsl:value-of select="numeroDeMusicas"/>  <br />
                            <strong><u><i>DATE:</i></u></strong> <xsl:text>  </xsl:text>
                            <xsl:value-of select="dataCriacao"/>
                        </td>
                        <td style="width: 120px;">
                            <button class="btn btn-outline-success dropdown-toggle" type="button" onclick="showHidenItens({$ID})">MUSICS
                            <span class="caret"></span></button>
                        </td>
                        <td style="width: 250px;">
                            <xsl:variable name="temp" select="id"/>
                            <button class="btn btn-outline-danger" type="button" onclick="location.href='http://127.0.0.1:8000/delete?id={$temp}'" onmouseover="this.style.color='white';" onmouseout="this.style.color='';">
                                Remove
                            </button>
                        </td>
                        <td id="{$ID}" style="display:none" class="dropdown"><br />
                            <ul>
                            <xsl:for-each select="musicas/musica">
                                <li>
                                    <img style="width: 40px; height: 40px;">
                                    <xsl:attribute name="src">
                                        <xsl:value-of select="img"/>
                                    </xsl:attribute>
                                    </img>
                                    <xsl:variable name="spotify" select="externalUrl"/>
                                    <a href="{$spotify}" target="_blank">
                                        <xsl:text>  </xsl:text>
                                        <xsl:value-of select="nome"/>
                                    </a>
                                </li>
                                <br/>
                            </xsl:for-each>
                            </ul>
                        </td>
                    </tr>
                </xsl:for-each>
                </tbody>
            </table>
    </xsl:template>
</xsl:stylesheet>